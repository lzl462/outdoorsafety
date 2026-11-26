# Outdoor Safety · Sea-to-Sky

A simple public website with checklists, “what to do if…” guides, common mistakes, and emergency numbers for outdoor trips in British Columbia’s Sea-to-Sky corridor.

## Turn the website on

The site is already on. GitHub Pages publishes it from the `main` branch, from the root folder, not from GitHub Actions. After a change is pushed to `main`, wait about a minute, then open https://lzl462.github.io/outdoorsafety/

## Local preview

```bash
python3 -m http.server 8080
```

Then visit http://localhost:8080

## Editing and checks

The site uses static HTML, CSS and small JavaScript files, including the trip planner and rehearsal modules. No build step or runtime framework is required. Start public wording in `content.md`, then update the HTML. Keep the repeated header/footer consistent across the thirteen content pages and the 404 page.

Run the dependency-free structural check before committing:

```bash
python3 scripts/check_site.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

The checker covers local assets/links (including print and concept stylesheets), anchors, expected page structure, the shared disclaimer, the genuine Home quotation and the printable plan's field counts. The regression tests check missing/duplicate landmarks and the intentional redirect/poster layouts. Browser and print acceptance evidence is recorded in `PLAN.md`.

The trip planner's validation, text export and email encoding can also be checked with Node.js 18 or later; this is a development check, not a website runtime dependency:

```bash
node --test scripts/test_trip_plan.mjs
```

## Print and share a plan

`resources.html` gathers the online trip planner, blank print sheet, A6 sign preview/PDF and website QR. It is linked from the shared footer and About.

`trip-plan.html` uses browser-only form processing. It does not submit entries to a server or save them in site storage. Users review the generated text, copy it, open a plain-text email draft or print it. The print view uses compact labels and values from the same shared field formatting, rather than reproducing the plain text's blank lines. Short and normal filled examples fit one A4/Letter page; long notes continue without clipping. The website cannot confirm sending/receipt or monitor returns. E-mail handoff uses a conservative 2,000-character encoded-URI ceiling; longer plans retain their complete text for copying/printing. This is an app policy, not a claim that all mail clients share a specific limit. No attachment is added. Without JavaScript, the existing blank sheet remains available.

## Presentation practice

`presentation.html` provides thirteen short English parts, ordered by the recorded Capstone requirements and the teacher's five questions (who, why, what, core competencies, next steps). It explains Liz's interviews, work on the pages and Instagram management, with a concrete AI/GitHub/responsive-design learning example. Detailed timeline, hours and source context sit in optional notes. The guiding question expresses the approved project purpose; the original-file comparison follows when the user supplies that file. The default/full-outline view also works without JavaScript. The optional one-part mode has Previous/Next controls; demo pages open deliberately in new tabs so the rehearsal stays in place. A short cue sheet follows the same thirteen parts with keywords and Show prompts. Its copy button reads the visible notes for pasting into phone notes, with a manual-selection fallback. Choose one or two demos and keep the questions as reserve.

The final subdued Presentation menu item is a temporary aid, marked `data-presentation-link` in every shared menu. It can be removed later without deleting the page or changing the visitor routes. Review the presentation and its canonical `content.md` section whenever features, navigation or advice change; keep detailed speaking points, demo links and the short cue sheet/Show prompts in sync. A cross-page overlay tour is not part of the current implementation.

## Instagram drafts

The account is [@outdoorsafety48](https://www.instagram.com/outdoorsafety48/), as confirmed by the user on 26 Nov. [social/instagram/README.md](social/instagram/README.md) maps the seven post topics to website sources and records publication status separately from prepared exports. Captions, artwork source, nine post images and profile options are tracked together. Which posts are live is awaiting confirmation. The renderer's original sandbox path is a known maintenance follow-up.

## Images, fonts and printing

Photographs and fonts are hosted locally. Photo credits and licences are in `images/README.md` and on About; the font licences are in `fonts/`. Photos are regional context, not images of the reported incidents.

Packing checks use browser storage when available and remain optional. The site has no offline mode. Guide pages can be printed or saved through the browser's PDF dialog; the separate handwritten trip plan fits one A4 or Canadian Letter page in the tested Chromium output. Filled online plans can use additional pages so long notes are not cut off.

The 404 page uses the `/outdoorsafety/` project prefix so links and assets also work on nested missing URLs. Update that prefix if the publishing path changes.
