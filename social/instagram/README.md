# Instagram drafts and publication record

The account is [@outdoorsafety48](https://www.instagram.com/outdoorsafety48/), confirmed by the user on 26 Nov 2026. Three posts are fully designed for launch: the website introduction (01), Before your trip (02) and If lost (04). Their image, caption and accessibility text are ready for manual upload. The other four topics retain reviewed copy and draft artwork for later. Publication dates and post URLs have not been supplied; prepared files do not establish that a post is live.

## Three finished posts: upload packages

All nine post images now use **1080 × 1080 pixels (1:1)**. Download the [new JPG upload package](instagram-upload-square.zip), extract it, then upload the individual files ending in `-square-1080.jpg`. These distinct names help avoid selecting an older cropped download. The design, colours, photographs and wording are retained. Captions and alt text remain in the files linked below. The first three launch topics are ready; the other topics retain their draft status. Matching [square PNGs](instagram-posts-square.zip) are also available.

The complete artwork fits in each square. Text stays within the centred 810-pixel-wide area, with at least 24 pixels above and below, so a centred 3:4 profile-preview crop also preserves it. [Profile-grid preview](profile-grid-preview.png) simulates that crop; [overview](overview.png) shows the complete square files. Neither comparison sheet is an image to upload.

Select a feed **Post**, keep the full square image selected and avoid zooming in. Post 07 uses its three square slides in order in one carousel. Check the app's upload preview before sharing. Stories and Reels require a separate layout. This change addresses crop handling; the exact cause in the user's app and the live account's final crop have not been observed.

| Post | Image | Caption ready to copy | Accessibility text |
| --- | --- | --- | --- |
| 01 · Website introduction | [PNG](posts/01-intro.png) | [Caption](launch-caption.txt) | [Alt text](launch-alt-text.txt) |
| 02 · Before your trip | [PNG](posts/02-before-you-go.png) | [Caption](before-your-trip-caption.txt) | [Alt text](before-your-trip-alt-text.txt) |
| 04 · If lost | [PNG](posts/04-if-lost.png) | [Caption](if-lost-caption.txt) | [Alt text](if-lost-alt-text.txt) |

The finished set uses the website's pine/lime visual identity. Post 01 promotes the guides; Post 02 gives preparation checks and the trusted contact's agreed calling deadline; Post 04 gives clear lost-person actions. Personal/school framing is retained in the website's About and presentation context. Upload the selected image and caption manually, add the alt text in the account's accessibility field, then record the resulting post URL/date below. The link-in-bio prompt assumes https://lzl462.github.io/outdoorsafety/ is set in the profile's link field; the full address is also included in the launch caption.

For the profile website field, copy **https://lzl462.github.io/outdoorsafety/** exactly; suggested link title: **Outdoor Safety — Sea-to-Sky**. The URL returned HTTP 200 on 27 Nov 2026. This is the destination for the website prompt, distinct from the Instagram account URL. Adding it to the account has not been confirmed.

## Files to maintain

| File or folder | Purpose |
| --- | --- |
| [captions.md](captions.md) | Reviewed profile/bio draft, seven captions and separate alt text for each topic. |
| `launch-*.txt`, `before-your-trip-*.txt`, `if-lost-*.txt` | Separate caption and accessibility-text handoff files for the three finished posts. |
| `posts/` | Nine 1080 × 1080 square PNG exports: six single-image posts and one three-slide carousel. |
| `upload-square/` | The same nine square artworks as quality-95 RGB JPGs, named `*-square-1080.jpg`. |
| [instagram-upload-square.zip](instagram-upload-square.zip) | New JPG upload package; extract before selecting the individual images. |
| [instagram-posts-square.zip](instagram-posts-square.zip) | The same nine individual PNGs, bundled for download; extract before uploading. |
| `profile/` | Two 1080 × 1080 profile options and a circle-crop comparison. The selected account image is not recorded yet. |
| [overview.png](overview.png) | Contact sheet for reviewing the kit; this is not a post to upload. |
| [profile-grid-preview.png](profile-grid-preview.png) | Centred 3:4 crop comparison of all nine square images; review only. |
| [src/build.py](src/build.py) | Generator holding the artwork wording, shared layout and rendering commands. |
| `src/*.html` | Generated artwork previews, with local fonts and two photographs. |
| [qr-website.svg](qr-website.svg) | A copy of the website QR. It opens the website, not the Instagram account. |
| [Instagram QR SVG](../../images/qr-instagram.svg), [PNG](../../images/qr-instagram.png), [print PDF](../../images/qr-instagram-print.pdf) | The separate account QR opens `https://www.instagram.com/outdoorsafety48/`. The SVG scales for the trifold board; the PNG is 1480 × 1480 and the PDF is a 100 mm square. |

Source advice stays in [content.md](../../content.md), with references on [About](../../about.html#sources). Campaign headings and captions are adaptations; they do not need to repeat the website sentence for sentence. The revised copy keeps the agreed 9-1-1 calling deadline explicit in the contact reminders, preserves the ten shared essentials and retains specialist contact numbers checked against primary sources. Existing photo and font credit/licence records remain in [images/README.md](../../images/README.md) and [fonts/](../../fonts/).

## Publication record

Each row is one post. Post 07 uses all three images in order in one carousel. Add a date and live URL only after a publication is confirmed; a committed PNG does not establish publication.

| ID | Prepared image(s) | Website source | Draft state | Publication date / URL |
| --- | --- | --- | --- | --- |
| 01 | [Website introduction](posts/01-intro.png) | [Home](../../index.html), [About](../../about.html#why-this-site) | Full visual design + reviewed copy, ready for manual upload | Not reported |
| 02 | [Before your trip](posts/02-before-you-go.png) | [Before your trip](../../checklists.html) | Full visual design + reviewed copy, ready for manual upload | Not reported |
| 03 | [Shared essentials](posts/03-pack-list.png) | [Shared essentials](../../pack-lists.html#essentials) | Reviewed copy; artwork draft | Not reported |
| 04 | [If lost](posts/04-if-lost.png) | [What to do if](../../if.html#lost) | Full visual design + reviewed copy, ready for manual upload | Not reported |
| 05 | [No service](posts/05-no-service.png) | [No cell service](../../no-service.html) | Reviewed copy; artwork draft | Not reported |
| 06 | [Emergency numbers](posts/06-emergency-numbers.png) | [Emergency numbers](../../emergency.html) | Reviewed copy/number check; artwork draft | Not reported |
| 07 | [Slide 1](posts/07-mistakes-1.png), [slide 2](posts/07-mistakes-2.png), [slide 3](posts/07-mistakes-3.png) | [Common mistakes](../../mistakes.html) | Reviewed copy; artwork draft | Not reported |

## Updating a post

1. Start advice/wording changes in `content.md` and keep the corresponding website page accurate.
2. Update the affected caption, alt text and artwork text in `src/build.py` together. `src/*.html` are generated; editing only one of them would be overwritten by the generator. When one of the three finished posts changes, refresh its separate plain-text caption/alt files from the reviewed copy.
3. Regenerate and inspect the affected HTML/PNG, including its footer, small-screen readability and the complete three-slide sequence. The renderer checks every text rectangle against the full export and the centred profile-preview safe area, then refreshes `overview.png`, `profile-grid-preview.png`, the square-image ZIP and the profile crop comparison.
4. Commit the related wording, source, exports and caption together. Upload the selected PNG(s) and caption manually; update the publication row with the confirmed date and URL. If a published post is edited later, record that change too.
5. When project status or features change, keep the presentation's detailed notes and cue sheet current as required by [AGENTS.md](../../AGENTS.md).

## Building the artwork

The renderer derives its paths from the repository. Full rendering uses Python with Pillow and Node with Playwright/Chromium available. These are development tools for image exports; the website still has no runtime framework or build dependency.

```sh
python3 social/instagram/src/build.py
python3 social/instagram/src/build.py --html-only
python3 social/instagram/src/build.py --only 01-intro
python3 social/instagram/src/build.py --previews-only
```

The default writes eleven HTML previews and renders nine square post images as PNG and JPG, plus two profile PNG options, then refreshes the overview, profile-grid/circle-crop comparisons and both ZIPs. JPGs are exported from the same fully loaded browser layout at quality 95; the PNG and JPG therefore share dimensions and composition. The existing 1080 × 1350 design canvas is fitted proportionally into a 1080 × 1080 square at 74% scale, rather than cut down. The centred 3:4 test crop runs from x=135 to x=945; the renderer requires all post text to stay inside that region and y=24 to y=1056. Profile icons retain their separate circular-crop workflow.

`--html-only` updates the artwork previews; `--only` limits PNG rendering to the named artwork; `--previews-only` rebuilds review previews and the ZIP from the existing square PNGs. Rebuild all posts together when changing the shared format so a carousel cannot mix dimensions.

Optional configuration: `--cdp URL` renders in an isolated context of an existing Chromium browser; `--browser PATH` selects a browser executable for a new instance; `--playwright-module PATH` (or `PLAYWRIGHT_MODULE`) locates a separately installed Playwright module. No account credentials belong in these files.
