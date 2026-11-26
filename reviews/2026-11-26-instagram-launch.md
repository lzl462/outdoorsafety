# Instagram launch, website access and display QR — 26 Nov 2026

The user requested a compact, professional website-promoting first post, then chose three fully finished launch posts rather than polishing every draft. Three parallel agents handled design/rendering, editorial/source review and website/QR integration. The coordinator registered public wording in content.md first, reviewed the final graphics and synchronized the presentation, plan and production brief.

## Three ready posts

| Post | Purpose | Final assets |
| --- | --- | --- |
| 01 | Introduce the website through planning, packing and practical next steps. | [PNG](../social/instagram/posts/01-intro.png), [caption](../social/instagram/launch-caption.txt), [alt text](../social/instagram/launch-alt-text.txt). |
| 02 | Prepare before a trip: route/group/conditions, essentials, turnaround and the trusted contact's calling deadline. | [PNG](../social/instagram/posts/02-before-you-go.png), [caption](../social/instagram/before-your-trip-caption.txt), [alt text](../social/instagram/before-your-trip-alt-text.txt). |
| 04 | Stop when lost, stay together/stay put unless unsafe, call 9-1-1 early, share location/incident and follow instructions. | [PNG](../social/instagram/posts/04-if-lost.png), [caption](../social/instagram/if-lost-caption.txt), [alt text](../social/instagram/if-lost-alt-text.txt). |

All three are new 1080 × 1350 designs with readable hierarchy, website address and link-in-bio prompt, using the site's pine/lime/paper system. Launch artwork and captions omit Liz/school/Capstone framing. The first graphic retains the licensed Stawamus Chief photograph and credit; the other two are code-native layouts. The lost-location exception applies to staying put, not to separating the group. Clear 9-1-1 guidance is retained.

Four other topics remain drafts, with source-aligned reviewed copy. Their retained numbers were checked by the editorial agent against [BC DPIC](https://www.dpic.org/contact), [BC Wildfire Service](https://blog.gov.bc.ca/bcwildfire/what-happens-when-you-report-a-wildfire-to-1-800-663-5555/) and [Canadian Coast Guard Radio Aids](https://www.canada.ca/en/canadian-coast-guard/corporate/publications/radio-aids-marine-navigation/general.html). These are existing contact details, not new medical advice. Navigation/communication and the agreed emergency calling deadline were clarified where needed.

The user chose to upload manually. The ready PNG/TXT packages do not establish publication. The website should be set in the Instagram profile's link field; the caption also includes its complete address. Confirmed post URLs/dates belong in the publication table after upload.

## Website and QR

Instagram appears in all fourteen shared footers, on About and in a new Print & share card. The Instagram QR directly encodes `https://www.instagram.com/outdoorsafety48/`. SVG and a 1480-pixel PNG retain a four-module white quiet zone; the PDF is one 100 mm square page. All three actual outputs were independently decoded. Existing website and trail-start destinations are unchanged.

The presentation's detailed notes and cue sheet now distinguish the display's website/Instagram codes from the trail sign's Quick reminders destination. The [large-display brief](../poster/README.md) records panel content roles and the separate remaining work: actual dimensions, full-size artwork, print files, printing and assembly. The rough hand sketch and old safety-poster reference do not establish a finished project board. Separate physical-printer tests remain excluded.

## Renderer and verification

The artwork generator is now repository-relative. It supports selected PNG exports, HTML-only generation and an isolated Chromium context, with configurable Playwright/browser paths. Overview and profile-crop previews regenerate with exports. Missing fonts/images abort export; development tooling does not add a website runtime dependency.

- All eleven generated HTML files match the source generator; all nine post PNGs and two profile options have their exact target dimensions. Browser rendering checked fonts, image/background completion and text bounds. The three finished posts and contact sheet were visually reviewed by the designer, editorial reviewer and coordinator.
- Final caption/alt TXT packages match captions.md and canonical wording. All thirteen presentation speaking-point lists and cue rows match content.md; rehearsal navigation, copying/manual fallback and no-JavaScript access pass.
- Chromium: fourteen footers at 320/390/768/1440 pixels, Resources layouts/accessibility, and actual SVG/PNG/PDF download-byte checks passed. WebKit passed the new Resources/About/Presentation layouts at the same widths. Selected automated accessibility rules are bounded checks, not full certification.
- The site check passes twenty public HTML files and 740 local references; nine structural regression tests pass. QR checks decode the actual SVG, PNG and PDF to the same exact URL.

No Instagram post was sent. Existing Git/SSH/credential settings remain unchanged.
