// Development exporter: static layout, twelve vector card PDFs and print kit.
import path from "node:path";
import fs from "node:fs/promises";
import assert from "node:assert/strict";
import { fileURLToPath, pathToFileURL } from "node:url";
import { spawnSync } from "node:child_process";
const args = process.argv.slice(2);
const option = (name) => {
  const i = args.indexOf(name);
  return i < 0 ? undefined : args[i + 1];
};
if (args.includes("--help")) {
  console.log(
    "node poster/render-preview.mjs [--layout-only] [--monochrome] [--cdp URL] [--playwright-module PATH] [--python PATH]",
  );
  process.exit(0);
}
const directory = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(directory, "..");
const source = JSON.parse(
  await fs.readFile(path.join(directory, "layout.json"), "utf8"),
);
const b = source.board,
  p = source.paper,
  s = source.spacing;
assert(
  p.name === "Legal" && p.widthMm === 215.9 && p.heightMm === 355.6,
  "This print kit requires Legal paper",
);
const board = {
  widthMm: b.leftMm + b.centreMm + b.rightMm,
  heightMm: b.heightMm,
  ...b,
};
const short = p.widthMm - 2 * p.marginMm,
  long = p.heightMm - 2 * p.marginMm;
const centreWidth = 2 * long + s.centreColumnGapMm,
  centreHeight = 4 * short + 3 * s.rowGapMm;
assert(
  centreWidth <= b.centreMm && centreHeight <= b.heightMm,
  "Print cards exceed centre panel",
);
assert(
  short < b.leftMm && short < b.rightMm && 2 * long + s.rowGapMm <= b.heightMm,
  "Print cards exceed side panels",
);
const cards = source.cards.map((card) => {
  const portrait = card.panel !== "centre";
  const widthMm = portrait ? short : long,
    heightMm = portrait ? long : short;
  const panelLeft =
    card.panel === "left"
      ? 0
      : card.panel === "right"
        ? b.leftMm + b.centreMm
        : b.leftMm;
  const panelWidth =
    card.panel === "left"
      ? b.leftMm
      : card.panel === "right"
        ? b.rightMm
        : b.centreMm;
  const xMm = portrait
    ? panelLeft + (panelWidth - short) / 2
    : b.leftMm +
      (b.centreMm - centreWidth) / 2 +
      card.column * (long + s.centreColumnGapMm);
  const yMm = portrait
    ? (b.heightMm - (2 * long + s.rowGapMm)) / 2 +
      card.row * (long + s.rowGapMm)
    : (b.heightMm - centreHeight) / 2 + card.row * (short + s.rowGapMm);
  assert(
    xMm >= panelLeft &&
      xMm + widthMm <= panelLeft + panelWidth &&
      yMm >= 0 &&
      yMm + heightMm <= b.heightMm,
  );
  return { ...card, widthMm, heightMm, xMm, yMm, portrait };
});
for (const a of cards)
  for (const c of cards)
    if (a.number < c.number)
      assert(
        a.xMm + a.widthMm <= c.xMm ||
          c.xMm + c.widthMm <= a.xMm ||
          a.yMm + a.heightMm <= c.yMm ||
          c.yMm + c.heightMm <= a.yMm,
        "Cards overlap",
      );
const manifest = { board, paper: p, cards };
const scratch = path.join(directory, ".render");
const variants = args.includes("--monochrome") ? [true] : [false, true];
await fs.mkdir(scratch, { recursive: true });
await fs.writeFile(
  path.join(scratch, "layout.json"),
  JSON.stringify(manifest, null, 2) + "\n",
);
const n = (value) => Number(value.toFixed(4));
let css = `/* Generated from layout.json by render-preview.mjs. */\n.display-board{--board-width:${n(board.widthMm)};--board-height:${n(board.heightMm)};--left-panel:${n(b.leftMm)};--centre-panel:${n(b.centreMm)}}\n`;
for (const c of cards)
  css += `#card-${c.id}{--card-x:${n(c.xMm)};--card-y:${n(c.yMm)};--card-width:${n(c.widthMm)};--card-height:${n(c.heightMm)}}\n`;
await fs.writeFile(path.join(directory, "layout.css"), css);
if (args.includes("--layout-only")) {
  console.log("Wrote measured layout.css and print manifest.");
  process.exit(0);
}
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
const base = "http://outdoorsafety-display.test";
try {
  await context.route(base + "/**", (route) => {
    const relative = decodeURIComponent(
      new URL(route.request().url()).pathname,
    ).replace(/^\/+/, "");
    const file = path.resolve(root, relative);
    assert(file.startsWith(root + path.sep));
    return route.fulfill({ path: file });
  });
  const page = await context.newPage();
  await page.goto(base + "/checklists.html", { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.locator("main > .page-heading").screenshot({
    path: path.join(directory, "website-preview.png"),
    animations: "disabled",
  });
  for (const monochrome of variants) {
    const artDirectory = monochrome
      ? path.join(scratch, "monochrome")
      : scratch;
    await fs.mkdir(artDirectory, { recursive: true });
    const results = [];
    for (const card of cards) {
      await page.goto(base + "/poster/display.html", { waitUntil: "load" });
      await page.evaluate((id) => {
        const card = document.getElementById("card-" + id);
        assertCard(card);
        function assertCard(value) {
          if (!value) throw new Error("Missing print card");
        }
        document.querySelector("main").replaceChildren(card);
      }, card.id);
      if (monochrome) {
        await page.addStyleTag({
          content: await fs.readFile(
            path.join(directory, "monochrome.css"),
            "utf8",
          ),
        });
        await page.evaluate((base) => {
          document.body.classList.add("monochrome");
          for (const image of document.images) {
            if (image.src.endsWith("/images/mark.svg")) {
              image.src = base + "/poster/mark-monochrome.svg";
            }
          }
          const credit = document.querySelector(".photo-card figcaption");
          if (credit)
            credit.textContent =
              credit.textContent.trim().replace(/\.$/, "") + " · Greyscale.";
        }, base);
      }
      await page.addStyleTag({
        content: `@page{size:${card.widthMm}mm ${card.heightMm}mm;margin:0}html,body,main{margin:0!important;padding:0!important;width:${card.widthMm}mm!important;height:${card.heightMm}mm!important;background:white}#card-${card.id}{--u:1mm;left:0!important;top:0!important;width:${card.widthMm}mm!important;height:${card.heightMm}mm!important}`,
      });
      await page.emulateMedia({ media: "print" });
      await page.evaluate(async () => {
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
          throw new Error("Print font failed to load");
        await document.fonts.ready;
        await Promise.all([...document.images].map((image) => image.decode()));
      });
      const failures = await page.locator("#card-" + card.id).evaluate((el) => {
        const card = el.getBoundingClientRect(),
          failures = [];
        const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
        let node;
        while ((node = walker.nextNode())) {
          if (!node.textContent.trim()) continue;
          const range = document.createRange();
          range.selectNodeContents(node);
          for (const box of range.getClientRects())
            if (
              box.width > 0.5 &&
              (box.left < card.left - 0.75 ||
                box.right > card.right + 0.75 ||
                box.top < card.top - 0.75 ||
                box.bottom > card.bottom + 0.75)
            )
              failures.push(node.textContent.trim());
        }
        const absolute = el.querySelector(
          ".source-notes,.terrain-mark,.trail-mark,.site-disclaimer",
        );
        if (absolute) {
          const top = absolute.getBoundingClientRect().top;
          for (const child of el.children)
            if (
              child !== absolute &&
              getComputedStyle(child).position !== "absolute" &&
              child.getBoundingClientRect().bottom > top + 0.75
            )
              failures.push("Normal content overlaps anchored content");
        }
        return failures;
      });
      assert.deepEqual(failures, [], card.id + " print clipping/overlap");
      await page.pdf({
        path: path.join(artDirectory, card.id + ".pdf"),
        width: card.widthMm + "mm",
        height: card.heightMm + "mm",
        margin: { top: 0, left: 0, right: 0, bottom: 0 },
        printBackground: true,
        preferCSSPageSize: true,
        displayHeaderFooter: false,
      });
      results.push({
        id: card.id,
        widthMm: card.widthMm,
        heightMm: card.heightMm,
        clipping: failures,
      });
    }
    await fs.writeFile(
      path.join(artDirectory, "render-checks.json"),
      JSON.stringify(results, null, 2) + "\n",
    );
  }
} finally {
  await context.close();
  if (!endpoint) await browser.close();
}
const python =
  option("--python") ||
  process.env.OUTDOORSAFETY_PYTHON ||
  (process.platform === "win32" ? "python" : "python3");
for (const monochrome of variants) {
  const result = spawnSync(
    python,
    [
      path.join(directory, "make-print-kit.py"),
      ...(monochrome ? ["--monochrome"] : []),
    ],
    {
      stdio: "inherit",
    },
  );
  assert.equal(result.status, 0, "Print-kit assembly failed");
}
console.log(
  "Exported twelve measured cards, Legal print set, assembly guide and previews for the selected print variants.",
);
process.exit(0);
