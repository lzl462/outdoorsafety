# Instagram drafts and publication record

The user confirmed on 26 Nov 2026 that the project account exists. Its actual handle is awaiting confirmation; `outdoorsafety48` in the first kit was a suggestion. Publication dates and URLs have not been supplied. Keep those states separate from the existence of prepared images.

## Files to maintain

| File or folder | Purpose |
| --- | --- |
| [captions.md](captions.md) | Profile/bio drafts and the caption for each numbered post. |
| `posts/` | Nine 1080 × 1350 PNG exports: six single-image posts and one three-slide carousel. |
| `profile/` | Two 1080 × 1080 profile options and a circle-crop comparison. The selected account image is not recorded yet. |
| [overview.png](overview.png) | Contact sheet for reviewing the kit; this is not a post to upload. |
| [src/build.py](src/build.py) | Generator holding the artwork wording, shared layout and rendering commands. |
| `src/*.html` | Generated artwork previews, with local fonts and two photographs. |
| [qr-website.svg](qr-website.svg) | A copy of the website QR. It opens the website, not the Instagram account. |

Source advice stays in [content.md](../../content.md), with references on [About](../../about.html#sources). Campaign headings and captions are adaptations. Existing photo and font credit/licence records remain in [images/README.md](../../images/README.md) and [fonts/](../../fonts/).

## Publication record

Each row is one post. Post 07 uses all three images in order in one carousel. Add a date and live URL only after a publication is confirmed; a committed PNG does not establish publication.

| ID | Prepared image(s) | Website source | Publication date / URL |
| --- | --- | --- | --- |
| 01 | [Intro](posts/01-intro.png) | [Home](../../index.html), [About](../../about.html#why-this-site) | Not reported |
| 02 | [Before you go](posts/02-before-you-go.png) | [Before your trip](../../checklists.html) | Not reported |
| 03 | [Pack list](posts/03-pack-list.png) | [Shared essentials](../../pack-lists.html#essentials) | Not reported |
| 04 | [If lost](posts/04-if-lost.png) | [What to do if](../../if.html#lost) | Not reported |
| 05 | [No service](posts/05-no-service.png) | [No cell service](../../no-service.html) | Not reported |
| 06 | [Emergency numbers](posts/06-emergency-numbers.png) | [Emergency numbers](../../emergency.html) | Not reported |
| 07 | [Slide 1](posts/07-mistakes-1.png), [slide 2](posts/07-mistakes-2.png), [slide 3](posts/07-mistakes-3.png) | [Common mistakes](../../mistakes.html) | Not reported |

## Updating a post

1. Start advice/wording changes in `content.md` and keep the corresponding website page accurate.
2. Update the affected caption and the artwork text in `src/build.py` together. `src/*.html` are generated; editing only one of them would be overwritten by the generator.
3. Regenerate and inspect the affected HTML/PNG, including its footer, small-screen readability and the complete three-slide sequence. Refresh `overview.png` when artwork changes; it is a separate preview, not an output currently produced by `build.py`.
4. Commit the related wording, source, exports and caption together. Upload the selected PNG(s) and caption manually; update the publication row with the confirmed date and URL. If a published post is edited later, record that change too.
5. When project status or features change, keep the presentation's detailed notes and cue sheet current as required by [AGENTS.md](../../AGENTS.md).

The current renderer still assumes `/workspace/instagram-kit` and `google-chrome`. Making its paths work from this checkout is a recommended follow-up before the next regeneration. Existing exports can be reviewed and uploaded now. No account credentials belong in these files.
