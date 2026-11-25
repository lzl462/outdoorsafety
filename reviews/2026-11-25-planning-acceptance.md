# Print & share and online trip plan — 25 Nov 2026

Implemented after Liz accepted the bounded proposal. This record covers the coordinator's implementation checks, not a new independent-agent review.

## Result

- Print & share is linked from the shared footer (including the project-prefixed 404) and About. It offers the online plan, existing blank sheet, labelled sign preview/A6 PDF and home-page QR.
- Before you leave offers online and printable paths. The existing blank print sheet gained a screen-only navigation link; its fields, equipment lines and print CSS are retained.
- The online form retains the trip/contact/equipment topics and explicitly separates expected return from the agreed calling deadline. Dates/times are treated as trip-local values, without converting them through the device's time zone. Missing essentials, impossible dates and contradictory time order are rejected without inventing a default waiting period.
- One plain-text representation feeds the read-only preview, copying, email body and print output. Changes invalidate the reviewed version. The calling deadline appears first, so lengthy route/medical notes cannot push it off the first printed page. Empty optional fields are labelled as not provided.
- Email opens a draft for the user to review/send. UTF-8, reserved characters and CRLF line breaks are encoded. There are no attachments, automatic sends, delivery/read confirmations, or return monitoring. A conservative 2,000-character encoded-URI ceiling selects the full-text copy fallback; content is never shortened to make a draft fit. This is a site policy rather than a universal client limit.
- The form makes no network submission and uses no site storage. Inputs are revealed only after the module initializes its handlers; a blocked module or disabled JavaScript retains the blank-sheet fallback. Clipboard failure selects the full text for manual copying.

## Checks

- Nine Python document-contract regression tests and five Node form-logic tests passed. The static checker passes 19 public HTML files and 620 local references, including the concept pages/stylesheets.
- Chromium: resources, online form, Before you leave and About passed text/overflow checks at 320, 390, 768 and 1440 pixels. Selected automated accessibility rules passed for resources and the empty form at 320/1440, plus the completed review state.
- Chromium reader journeys covered resource-to-sign, preparation-to-online-plan, missing-field focus, invalid deadline/correction, review, exact email-body/preview equality, copying and manual-copy fallback, stale-review invalidation, long-plan fallback and clearing. A real browser clipboard write/read preserved the complete reviewed text with native Windows line endings. Plan fields do not impose character caps that would silently cut pasted route notes. Blocked storage did not prevent review; no plan data appeared in request URLs or POSTs. No real email was sent.
- WebKit: resources, online form and preparation layouts passed at the same four widths. Native date/time inputs, review and complete Unicode email-body handoff were exercised. No native Apple-device claim is made.
- Actual Chromium PDF exports: the standard short filled example is one A4 page; the long example is two pages and retains its ending, optional details, deadline and disclaimer. The deadline stays on page one. The blank sheet remains one page on both A4 and Canadian Letter. Filled-plan pagination is allowed to grow rather than lose content.
- The sign's QR was decoded from its actual A6 PDF and PNG during the preceding concept pass; it points to `tips.html`. That artwork and PDF remain unchanged. Print & share labels the design as a concept; the shorter briefing preview does not replace Quick reminders.

## Limits

The automated tests did not exercise external mail applications or end-to-end email delivery. Browser tests intercepted the handoff and checked the complete URI contents; the UI always provides copying and explains that the user must send and confirm receipt. These statements describe the automated checks, not the subsequent user acceptance below. The site has no offline support. Visitor symbol recognition, optional native iPhone/iPad checks, existing personal/school completion work and multilingual ideas remain separate.

## Subsequent user acceptance — 25 Nov 2026

The user reported testing the email and QR functions and confirmed that both are adequate for this school project's scope. Mark these practical functional checks complete; the device and test method were not specified. This does not add automated sending, receipt confirmation or return monitoring to the website.

The user explicitly excluded physical printer tests because no printer is available. They are not an outstanding acceptance task. The completed browser-generated PDF checks remain recorded; no physical printer run is claimed or required.

## Filled-plan print correction — 26 Nov 2026

The user reported that a filled online plan unnecessarily occupied two pages. Reproduced this with a normal 1,167-character plan containing a two-line route, three phone numbers and eight equipment lines: both A4 and Letter used two pages. The earlier short-only acceptance fixture did not expose the excessive whitespace.

Replaced the printed plain-text block with compact label/value rows. One shared formatter supplies all fifteen fields to both the unchanged preview/email text and the print layout. Print uses readable 11-point values, bold labels and a bordered calling deadline at the top. User line breaks remain; lengthy notes can continue onto further pages. The separate blank sheet is unchanged. Presentation Show prompts and the short cue sheet now include compact printing.

| Chromium PDF fixture | Before: A4 / Letter | After: A4 / Letter |
| --- | --- | --- |
| Short filled plan, 925 characters | 1 / 1 pages | 1 / 1 pages |
| Normal filled plan, 1,167 characters | 2 / 2 pages | 1 / 1 pages |
| Long route notes, 10,172 characters | 3 / 3 pages | 3 / 3 pages |

PDF text checks retain every reviewed paragraph and all long-note endings; the deadline remains on page one. The normal A4 rendering was visually inspected. These exports include a browser page-number footer. Preview/copy/email text is byte-for-byte unchanged across the three fixtures.

Chromium and WebKit checks at 320, 390 and 1440 pixels covered all fifteen printed fields against the review, unchanged copying, the print button, browser-menu printing after edits, and clearing invalid/stale print content. Five form tests, nine structural tests and the site checker (20 HTML files, 721 local references) passed. Physical printer tests remain excluded.
