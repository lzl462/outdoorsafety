# Large trifold project display — design and production

The professional draft is ready: [interactive preview](display.html), [PNG preview](display-preview.png) and [PDF preview](display-preview.pdf). Visitors can reach it from Print & share and presentation part 8. On phones it stacks the panels for readable text; “View at full size” shows the board arrangement in a scrollable area.

It replaces Liz's rough hand sketch, which remains in Git history. The eight content areas retain that sketch's structure while explaining the whole project: purpose, interviews, website features, Liz's work and learning. Public wording is recorded in content.md and follows the [presentation](../presentation.html) and [approved-proposal comparison](../docs/school/README.md). The older [website safety-poster layout](../pdfs/trifold.html) remains a separate reference.

## Design, not final board dimensions

The design canvas is 2400 × 1800 units, with left/centre/right panel proportions of 1:2:1. The PNG is a high-resolution design preview; the single-page A3 landscape PDF is for reviewing the composition, with a concept note outside the board. These are not a measured print master or a chosen printing method. Actual cardboard dimensions and fold margins are still unknown.

The layout uses the website's local fonts, pine/lime colours and licensed Stawamus Chief photograph. It includes an actual “Before your trip” website preview and two separately labelled QR destinations. Photo credit stays on the board; source details remain on About. The display does not claim an organizational endorsement or completed trail installation.

## Content areas

| Area | Role |
| --- | --- |
| Left two boxes | Why the project matters; research and the two local rescue contributors. |
| Centre headline and large box | Project name and purpose; a website screenshot. |
| Centre two smaller boxes | Practical examples: Trip Plan and the trail-start QR concept. |
| Centre bottom row | Clearly labelled website QR, a brief website description and Instagram QR. |
| Right two boxes | Liz's interviews/page work and AI/GitHub/design learning; competencies and next steps. |

Keep the display wording and previews aligned with the canonical content and presentation when the project changes. The source HTML/CSS stays editable; JavaScript only controls the optional full-size view.

## Regenerate the previews

The development-only helper needs Node.js and Playwright with Chromium installed. If Playwright is available to Node's module resolver:

```bash
node poster/render-preview.mjs
```

Alternatively, point it at an existing development installation and, optionally, an already running Chromium debugging endpoint:

```bash
node poster/render-preview.mjs --playwright-module /path/to/playwright/index.mjs --cdp http://localhost:9026
```

The helper resolves repository paths from its own location, captures the full preparation-page heading, then exports the 4800 × 3600 board PNG and one-page A3 landscape review PDF. `--help` lists its options. A connected browser keeps its existing tabs; the helper closes only its own context. Review text/layout and decode both exported QR codes after design changes. No build step or Playwright installation is needed to view the public page.

## Ready QR assets

- Website: [scalable print SVG](../images/qr-website-print.svg), opening the website home page.
- Instagram: [scalable SVG](../images/qr-instagram.svg), [PNG](../images/qr-instagram.png) and [100 mm PDF](../images/qr-instagram-print.pdf), opening `https://www.instagram.com/outdoorsafety48/`.
- Keep each code's white border and label its destination. Use the SVGs when placing them in the final display artwork; avoid stretching or cropping the codes.

## Remaining production work

1. Confirm the actual board's overall dimensions, each panel width and the fold/gutter margins. No final measurements have been supplied.
2. Review the draft against that board and decide the printing method: smaller sheets mounted on the cardboard, separate panel prints or a large-format print. No route is selected yet.
3. Adapt the design to the measured dimensions and any final content edits. Export a print master or the separate panels/sheets at the correct scale; retain readable type, fold clearances and QR white borders.
4. Arrange printing through the available school, print shop or other chosen route, then trim, mount and assemble the board. Printing/assembly are remaining deliverables, not completed work inferred from the preview.
5. Confirm the finished board is ready for the presentation. The earlier exclusion of separate physical-printer tests remains; this production task does not reopen that test requirement.
