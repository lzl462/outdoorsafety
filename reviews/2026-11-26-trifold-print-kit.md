# Measured trifold and Legal print kit — 26 November 2026

The user supplied an annotated photograph and requested a practical school-printing layout. Its centimetre labels read 129.54 cm high, 80.52 cm centre and 24.13 cm for the left wing. The right is unlabelled and provisionally matches the left. The open width is therefore 128.78 cm. The personal photo is not published. School Legal-paper availability remains an assumption to confirm, rather than a claim about a known printer.

## Design and delivery

The existing source-backed project story is arranged into twelve whole cards: four portrait on the wings and four landscape pairs in the centre. The eight original content roles remain; the title/photo and project/website-preview pairs now use their own cards. None crosses a fold. Each trimmed card is 19.05 × 33.02 cm, oriented for its placement. Locally hosted fonts, licensed Chief photograph, source/non-endorsement language and first-name-only student credit remain. No safety guidance or quotations were invented.

- [Legal print set](../poster/trifold-legal.pdf): twelve 612 × 1008-point portrait pages. Landscape card art is turned on the sheet; it turns back after trimming. Every page has half-inch margins to the trim rectangle, external card identification, crop marks and an exact 100 mm ruler.
- [Assembly guide](../poster/trifold-assembly.pdf): one portrait Legal page, with dimensions, fold positions, twelve numbered locations, centimetre placement table and printing instructions.
- [Full-size master](../poster/trifold-full-size.pdf): a vector page at 1287.8 × 1295.4 mm.
- [PNG](../poster/display-preview.png) and [A3 PDF](../poster/display-preview.pdf): review previews, distinguished from the actual-size print set.

The print instructions specify Legal, Actual size / 100%, portrait, single-sided and one page per sheet. The set is already divided into sheets, so Fit/Poster/Booklet is inappropriate. Card numbers are noted on the back before trimming, and QR white borders remain intact. Legal/Letter dimensions were checked against [HP's paper-size table](https://support.hp.com/us-en/document/ish_2761798-2817316-16). This establishes sizes, not the school printer's capabilities.

## Verification

- The source layout asserts fit within each panel and rejects overlaps. Chromium export checks all twelve cards for font/image completion, text bounds and collisions with anchored notes/icons.
- Compared every art page's text with the HTML, ignoring whitespace introduced by decorative letter spacing. All characters/punctuation are retained in both the print sheets and master. No text extends outside a paper page. Every ruler's actual PDF line is 100 mm; source-art dimensions match the intended cut sizes.
- Decoded the actual website and Instagram QR targets from print pages 9/10, the full master, the assembly guide, A3 preview and PNG. The two URLs are unchanged. New PDF metadata identifies only Liz.
- Chromium and WebKit passed display/resources checks at 320/390/768/1440 pixels: twelve visible cards, no text clipping or whole-page overflow, zoom control/state/contained scrolling, resource navigation/return and no-JavaScript reading. Selected Chromium accessibility rules passed at 320 and 1440 pixels.
- The presentation remains unlisted. All thirteen practice steps, twenty-one demos, copied cue text/manual fallback and no-JavaScript paths pass. Speaking points remain 820 words; the updated print-set cue makes the short sheet 139 words.
- Nine structural regression tests and the 21-page/751-reference site check pass. Representative composition, sheet, guide and mobile views were visually inspected.

## Remaining production boundary

Confirm the right wing and loaded Legal paper, then print, trim, position and mount the cards. The files do not establish a physical print run or assembled board. Separate mandatory physical-printer tests remain excluded as requested earlier. The unlisted rehearsal page is not reintroduced into public navigation.
