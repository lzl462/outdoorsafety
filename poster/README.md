# Trifold display — Legal print kit

The display is ready as a [measured preview](display.html), a [twelve-page Legal print set](trifold-legal.pdf) and a [one-page assembly guide](trifold-assembly.pdf). It remains reachable through Print & share. The unlisted presentation also has a deliberate demo link; public pages do not link to that rehearsal page.

## Working measurements

Measurements were transcribed from the user's annotated photo supplied on 26 November. The personal photo is not published.

| Part | Size |
| --- | --- |
| Board height | 129.54 cm |
| Left panel | 24.13 cm wide |
| Centre panel | 80.52 cm wide |
| Right panel | 24.13 cm wide, assumed equal to the left until confirmed |
| Open board | 128.78 cm wide × 129.54 cm high |

These are the supplied centimetre values; the right panel has no separate measurement in the photo. The assumed symmetry is visible in the preview and guide. Legal is the user's proposed school-printing route; the actual paper/tray has not been confirmed.

## Twelve complete cards

Each card is 19.05 × 33.02 cm after trimming. Four are mounted vertically on the wings; eight are mounted horizontally in the centre. Every print page is portrait Legal, with the horizontal cards turned on their sheets. This keeps the whole set printable in one batch using one paper orientation. Text and QR codes stay on individual sheets.

| Printed page | Content | Mounting position |
| --- | --- | --- |
| 01 / 02 | Title / licensed local photograph | Centre, first row |
| 03 / 04 | Why I chose this / local rescuers | Left, upper / lower |
| 05 / 06 | The project / website preview | Centre, second row |
| 07 / 08 | Trip Plan / trail-start QR idea | Centre, third row |
| 09 / 10 | Website QR / Instagram QR | Centre, fourth row |
| 11 / 12 | My work and learning / skills and next steps | Right, upper / lower |

The layout uses the white cardboard between the separate cards. The cards clear both folds; placement coordinates in the guide are measured from the upper-left corner with the board open and flat. All card art keeps the confirmed project wording, first-name-only student credit and photo/source attribution. The two QR destinations remain distinct.

## Printing at school

1. Confirm that the loaded paper is **Legal, 8.5 × 14 in (215.9 × 355.6 mm)**. Letter is 8.5 × 11 in and is shorter. The dimensions are documented by [HP](https://support.hp.com/us-en/document/ish_2761798-2817316-16); this does not establish which school printer/tray is available.
2. Download **trifold-legal.pdf**, rather than printing the web preview or the A3 review PDF.
3. Print pages 1–12 in colour, **portrait**, **single-sided**, **Actual size / 100%**, **one page per sheet**. Do not use Fit, Poster, Booklet or multiple pages per sheet: the PDF already contains the individual cards. Page size is 612 × 1008 PDF points on all twelve pages.
4. Keep the sheet labels until sorting is complete. Write each card's number on its back, then trim on the crop marks. The 100 mm scale line is outside the artwork. Turn the eight landscape cards after cutting. Leave every QR code's white border intact.
5. Place the cards on the open, flat board using the assembly guide, then mount and fold. The guide lists each card's panel, position and final orientation.

The PDF artwork has conservative half-inch margins to the trim rectangle; no borderless printer is required. Actual printer scaling, paper availability, printing and mounting are physical production steps still to be completed. The earlier exclusion of separate physical-printer tests remains; no physical print run is claimed.

## Files

- [trifold-legal.pdf](trifold-legal.pdf): twelve actual-size Legal sheets, with card numbers, crop marks and scale lines outside the finished artwork.
- [trifold-assembly.pdf](trifold-assembly.pdf): one Legal page with board dimensions, folds, card map, placement coordinates and print settings.
- [trifold-full-size.pdf](trifold-full-size.pdf): one page at the complete board's physical dimensions, for reference or a separately chosen large-format route.
- [display-preview.png](display-preview.png): high-resolution composition preview, not a paper-size template.
- [display-preview.pdf](display-preview.pdf): one A3 scaled review page, explicitly labelled as a preview.
- `display.html` / `display.css`: editable card wording and visual design. The mobile view reflows for reading; the full-size view preserves the board arrangement.
- `layout.json`: board values, assumptions, paper size and card roles. `layout.css` is generated from it.

The old [safety-poster reference](../pdfs/trifold.html) remains separate from this project display. The rough hand sketch stays only in Git history.

## Regenerate together

Development dependencies are Node.js, Playwright with Chromium, and Python with PyMuPDF. The public site has no build dependency.

```bash
node poster/render-preview.mjs
```

For an existing development browser/environment:

```bash
node poster/render-preview.mjs --cdp http://localhost:9026 --playwright-module /path/to/playwright/index.mjs --python /path/to/python-with-pymupdf
```

`--layout-only` regenerates the measured CSS/manifest without a browser. Normal rendering captures the website heading, validates the twelve card exports for loaded fonts/images and text clipping/overlap, then calls `make-print-kit.py` to build all PDF/PNG outputs from the same vector artwork. Temporary artwork and check manifests live in ignored `.render/`. Only the helper's isolated context closes when connecting to an existing browser.

Start wording changes in content.md. Regenerate the print set, master, guide and previews together; inspect representative sheets and decode the actual exported QR codes. Keep presentation part 8 and its cue-sheet prompt current. Physical production remains separate from these digital checks.
