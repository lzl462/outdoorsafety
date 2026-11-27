import assert from "node:assert/strict";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const { chromium } = await import(
  process.env.PLAYWRIGHT_MODULE
    ? pathToFileURL(process.env.PLAYWRIGHT_MODULE).href
    : "playwright"
);
const browser = await chromium.launch();
const base = "http://outdoorsafety-menu.test";
let destinations = 0;
try {
  for (const viewport of [
    { width: 1440, height: 900 },
    { width: 390, height: 844 },
    { width: 844, height: 390 },
  ]) {
    const context = await browser.newContext({ viewport });
    await context.route(base + "/**", async (route) => {
      const relative = decodeURIComponent(new URL(route.request().url()).pathname);
      const file = path.resolve(root, "." + relative);
      assert(file.startsWith(root + path.sep));
      await route.fulfill({ path: file });
    });
    const page = await context.newPage();
    await page.goto(base + "/index.html");
    const links = await page.locator(".menu-panel a").evaluateAll((elements) =>
      elements.map((element) => element.getAttribute("href")),
    );
    for (const href of links) {
      await page.goto(base + "/index.html");
      await page.locator(".site-menu summary").click();
      await page.locator(`.menu-panel a[href="${href}"]`).click();
      await page.waitForURL(base + "/" + href);
      assert.equal(await page.locator("h1").count(), 1);
      destinations++;
    }
    await page.goto(base + "/index.html");
    const summary = page.locator(".site-menu summary");
    await summary.focus();
    await summary.press("Enter");
    await summary.evaluate((element) => element.blur());
    await page.evaluate(() => new Promise((resolve) => requestAnimationFrame(resolve)));
    assert(await page.locator(".site-menu").evaluate((element) => element.open),
      "Losing focus to the body must not dismiss a menu before a pointer click");
    await page.locator('.menu-panel a[href="trip-plan.html"]').click();
    await page.waitForURL(base + "/trip-plan.html");
    await page.locator(".site-menu summary").click();
    await page.locator(".site-menu summary").press("Escape");
    assert.equal(await page.locator(".site-menu").evaluate((element) => element.open), false);
    await page.locator(".site-menu summary").click();
    await page.mouse.click(2, viewport.height - 2);
    assert.equal(await page.locator(".site-menu").evaluate((element) => element.open), false);
    await page.locator(".site-menu summary").click();
    await page.locator(".brand").focus();
    assert.equal(await page.locator(".site-menu").evaluate((element) => element.open), false);
    await context.close();
  }
  const context = await browser.newContext({ javaScriptEnabled: false });
  await context.route(base + "/**", (route) => route.fulfill({
    path: path.join(root, new URL(route.request().url()).pathname),
  }));
  const page = await context.newPage();
  await page.goto(base + "/index.html");
  await page.locator(".site-menu summary").click();
  await page.locator('.menu-panel a[href="trip-plan.html"]').click();
  await page.waitForURL(base + "/trip-plan.html");
  await context.close();
  console.log(`${destinations} menu destinations, focus regression, dismissal and no-JS checks passed.`);
} finally {
  await browser.close();
}
