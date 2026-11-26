// Development export helper; the public display page has no build dependency.
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import assert from "node:assert/strict";

const args = process.argv.slice(2);
if (args.includes("--help")) {
  console.log(
    "node poster/render-preview.mjs [--cdp http://localhost:9026] [--playwright-module /path/to/playwright/index.mjs]",
  );
  process.exit(0);
}
const option = (name) => {
  const index = args.indexOf(name);
  return index >= 0 ? args[index + 1] : undefined;
};
const modulePath =
  option("--playwright-module") || process.env.PLAYWRIGHT_MODULE;
const { chromium } = await import(
  modulePath ? pathToFileURL(path.resolve(modulePath)).href : "playwright"
);
const endpoint = option("--cdp");
const browser = endpoint
  ? await chromium.connectOverCDP(endpoint)
  : await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1280, height: 900 },
  deviceScaleFactor: 2,
});
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const base = "http://outdoorsafety-display.test";
try {
  await context.route(base + "/**", (route) => {
    const relative = decodeURIComponent(
      new URL(route.request().url()).pathname,
    ).replace(/^\/+/, "");
    const file = path.resolve(root, relative);
    assert(
      file.startsWith(root + path.sep),
      "Preview asset escaped the repository",
    );
    return route.fulfill({ path: file });
  });
  const page = await context.newPage();
  await page.goto(base + "/checklists.html", { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.locator("main > .page-heading").screenshot({
    path: path.join(root, "poster/website-preview.png"),
    animations: "disabled",
  });
  await page.setViewportSize({ width: 2464, height: 2100 });
  await page.goto(base + "/poster/display.html", { waitUntil: "load" });
  await page.evaluate(async () => {
    await document.fonts.ready;
    const faces = await Promise.all(
      ["700 20px Display", "400 20px Body", "700 20px Body"].map((spec) =>
        document.fonts.load(spec),
      ),
    );
    if (
      faces.some(
        (group) =>
          !group.length || group.some((face) => face.status !== "loaded"),
      )
    )
      throw new Error("A display font failed to load.");
    await Promise.all([...document.images].map((image) => image.decode()));
  });
  const board = await page.locator("#display-board").boundingBox();
  assert.equal(Math.round(board.width), 2400);
  assert.equal(Math.round(board.height), 1800);
  await page.screenshot({
    path: path.join(root, "poster/display-preview.png"),
    animations: "disabled",
    clip: {
      x: Math.round(board.x),
      y: Math.round(board.y),
      width: 2400,
      height: 1800,
    },
  });
  await page.pdf({
    path: path.join(root, "poster/display-preview.pdf"),
    format: "A3",
    landscape: true,
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: false,
  });
  console.log(
    "Wrote poster/website-preview.png, display-preview.png (4800 × 3600), and the A3 landscape PDF preview.",
  );
} finally {
  await context.close();
  if (!endpoint) await browser.close();
}
// A connected browser belongs to its owner; only this helper's context is closed.
process.exit(0);
