# Trail-start sign concept

School-project design preview, 25 Nov 2026. The sign/PDF is available through Print & share. It has not been placed at a trailhead. The shorter briefing is a labelled preview, not a replacement of the existing Quick reminders page.

- [Sign preview](trail-sign.html): the A6 sign alongside its concept notes and print action.
- [Print PDF](trail-sign-a6.pdf): one A6 page, approximately 105 × 148 mm. Print at actual size for a size check; physical printing/scanning has not been tested.
- [Artwork preview](trail-sign-preview.png): raster preview for discussion; use the PDF for printing.
- [Short mobile briefing](trail-briefing.html): four preparation questions, direct emergency orientation and links into the existing site. It is a proposed evolution of the existing Quick reminders entry point.

From the repository root, run `python3 -m http.server 8080`, then visit `http://localhost:8080/prototypes/trail-sign.html`.

## Intent and destination

The mountain, walker and return arrow suggest an outing and getting back. “BIG VIEWS. SAFE RETURN.” is an invitation to prepare, not a claim that a scan guarantees safety. Symbol recognition and willingness to scan have not been tested with visitors. The sign uses the neutral project/region label “Outdoor Safety · Sea-to-Sky”; the preview and About explain the school project. No official trail-management or rescue-service status is claimed.

The real QR encodes **https://lzl462.github.io/outdoorsafety/tips.html**. Scanning opens the existing Quick reminders page rather than the briefing concept preview. If the shorter briefing is adopted, refine `tips.html` at the same address rather than changing the printed code's destination.

The mobile draft condenses the existing preparation/contact/no-service guidance in `content.md`; no equipment, story or emergency procedure was invented. Public draft copy was recorded there before the HTML was created; [AdventureSmart's Three Ts](https://www.adventuresmart.ca/the-three-ts/) were rechecked on 25 Nov. The sign/briefing are aimed at visitors at busy trail starts with reception. A first visit needs a connection to load the page; this adds no offline mode or emergency-alert capability.

## Assets and checks

`trail-symbol.svg` is an original code-drawn vector. Fonts reuse the repository's locally hosted Barlow Condensed and DM Sans and their existing licences. No external photo, analytics or QR-redirect service is used.

`qr-trail-sign.svg` was generated with Python qrcode 8.2, error correction Q and a four-module quiet zone. The square code has no logo overlay. The QR was independently decoded from both the PNG preview and the actual Chromium PDF using zxing-cpp 3.2.0; both yielded the exact live URL above. These are digital checks, not a field scan or a physical-print test.

The PDF and preview were exported from `trail-sign.html` after local fonts/images loaded, with print backgrounds enabled and CSS page size preferred. The Print button uses the same stylesheet. No browser header/footer should be added to this small sign.

## Deferred

- Decide whether to adopt the short briefing on the existing Quick reminders page after looking at this prototype; preserve useful detailed reminders and incoming links.
- Test the icon, small print and scan with real visitors/phones and a sample print before any real use. No physical placement is part of this prototype.
- Later, consider French, German, Spanish and Italian for the short briefing first, with main guides as a later expansion. Keep one stable QR, explicit language names and an English fallback; check that translations preserve the safety meaning. Do not show language choices until translations exist.
