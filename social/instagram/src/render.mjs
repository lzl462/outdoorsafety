// Development-only renderer. The public website has no Node/Playwright runtime.
import assert from "node:assert/strict";
import path from "node:path";
import { pathToFileURL } from "node:url";

let input = "";
for await (const chunk of process.stdin) input += chunk;
const config = JSON.parse(input);
const moduleName = config.playwrightModule
  ? pathToFileURL(path.resolve(config.playwrightModule)).href
  : "playwright";
let chromium;
try {
  ({ chromium } = await import(moduleName));
} catch {
  console.error(
    "Instagram PNG rendering needs Playwright. Install it as a development dependency, or pass --playwright-module /path/to/playwright/index.mjs.",
  );
  process.exit(1);
}
const launched = !config.cdp;
let browser;
try {
  browser = config.cdp
    ? await chromium.connectOverCDP(config.cdp)
    : await chromium.launch(
        config.browser ? { executablePath: config.browser } : {},
      );
} catch (error) {
  console.error(
    "Could not start or connect to Chromium. Check --cdp/--browser, or install the Playwright Chromium development browser.\n" +
      error.message,
  );
  process.exit(1);
}
let context;
const base = "http://outdoorsafety-artwork.test";
const results = [];
try {
  context = await browser.newContext({ deviceScaleFactor: 1 });
  const assetFailures = [];
  await context.route("**/*", async (route) => {
    const url = new URL(route.request().url());
    if (url.origin !== base) {
      assetFailures.push("External artwork asset: " + url.href);
      await route.abort();
      return;
    }
    const relative = decodeURIComponent(url.pathname).slice(1);
    if (relative === "favicon.ico") {
      await route.fulfill({ status: 204, body: "" });
      return;
    }
    const file = path.resolve(config.source, relative);
    assert(
      file.startsWith(path.resolve(config.source) + path.sep),
      "Artwork path escaped its source directory",
    );
    try {
      await route.fulfill({ path: file });
    } catch {
      assetFailures.push(relative);
      await route.abort();
    }
  });
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", (error) => errors.push(error.message));
  for (const target of config.targets) {
    await page.setViewportSize({ width: target.width, height: target.height });
    await page.goto(`${base}/${target.name}.html`, { waitUntil: "load" });
    try {
      await page.evaluate(async () => {
        const faces = await Promise.all(
          ["700 20px BC", "400 20px DM", "700 20px DM"].map((spec) =>
            document.fonts.load(spec),
          ),
        );
        if (
          faces.some(
            (group) =>
              !group.length || group.some((face) => face.status !== "loaded"),
          )
        ) {
          throw new Error("An artwork font failed to load.");
        }
        await document.fonts.ready;
        const backgrounds = new Set();
        for (const element of document.querySelectorAll("*")) {
          for (const match of getComputedStyle(
            element,
          ).backgroundImage.matchAll(/url\(["']?([^"')]+)["']?\)/g))
            backgrounds.add(match[1]);
        }
        await Promise.all([...document.images].map((image) => image.decode()));
        await Promise.all(
          [...backgrounds].map(async (url) => {
            const image = new Image();
            image.src = url;
            try {
              await image.decode();
            } catch {
              throw new Error("Artwork background could not decode: " + url);
            }
          }),
        );
      });
    } catch (error) {
      const detail = assetFailures.length
        ? "Missing: " + assetFailures.join(", ")
        : error.message;
      throw new Error(
        `${target.name}: artwork fonts or images failed to load. ${detail}`,
      );
    }
    assert.deepEqual(
      assetFailures,
      [],
      `${target.name}: missing artwork assets`,
    );
    const clipping = await page.evaluate((safeBounds) => {
      const walker = document.createTreeWalker(
        document.body,
        NodeFilter.SHOW_TEXT,
      );
      const failures = [];
      let node;
      while ((node = walker.nextNode())) {
        if (!node.textContent.trim()) continue;
        const range = document.createRange();
        range.selectNodeContents(node);
        for (const box of range.getClientRects()) {
          if (box.width < 0.5 || box.height < 0.5) continue;
          if (
            box.left < -0.5 ||
            box.top < -0.5 ||
            box.right > innerWidth + 0.5 ||
            box.bottom > innerHeight + 0.5
          ) {
            failures.push(node.textContent.trim().slice(0, 90));
          }
          if (safeBounds && (
            box.left < safeBounds.left - 0.5 ||
            box.top < safeBounds.top - 0.5 ||
            box.right > safeBounds.right + 0.5 ||
            box.bottom > safeBounds.bottom + 0.5
          )) failures.push("Outside crop-safe area: " + node.textContent.trim().slice(0, 90));
        }
      }
      return [...new Set(failures)];
    }, target.safeBounds);
    assert.deepEqual(clipping, [], `${target.name}: text outside export`);
    await page.screenshot({ path: target.output, animations: "disabled" });
    if (target.uploadOutput) {
      await page.screenshot({
        path: target.uploadOutput,
        type: "jpeg",
        quality: 95,
        animations: "disabled",
      });
    }
    results.push({
      name: target.name,
      width: target.width,
      height: target.height,
      clipping,
      safeBounds: target.safeBounds,
      uploadOutput: target.uploadOutput,
    });
  }
  assert.deepEqual(errors, [], "Artwork browser errors");
  console.log(JSON.stringify({ rendered: results }));
} finally {
  if (context) await context.close();
  if (launched) await browser.close();
}
// Disconnecting from an existing browser must not close its other contexts.
process.exit(0);
