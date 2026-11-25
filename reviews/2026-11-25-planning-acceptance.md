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

Actual external mail applications and end-to-end email delivery were not exercised. Browser tests intercepted the handoff and checked the complete URI contents; the UI always provides copying and explains that the user must send and confirm receipt. Physical printing/phone scans, visitor symbol recognition and native iPhone/iPad testing remain unverified. The site has no offline support. Existing personal/school completion work and multilingual ideas remain separate.
