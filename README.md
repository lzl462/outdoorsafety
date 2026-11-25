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

The site uses static HTML, CSS and a small JavaScript file. No build step or runtime framework is required. Start public wording in `content.md`, then update the HTML. Keep the repeated header/footer consistent across the ten content pages and the 404 page.

Run the dependency-free structural check before committing:

```bash
python3 scripts/check_site.py
```

The checker covers local assets/links, anchors, page structure, the shared disclaimer, the genuine Home quotation and the printable plan's field counts. Browser and print acceptance evidence is recorded in `PLAN.md`.

## Images, fonts and printing

Photographs and fonts are hosted locally. Photo credits and licences are in `images/README.md` and on About; the font licences are in `fonts/`. Photos are regional context, not images of the reported incidents.

Packing checks use browser storage when available and remain optional. The site has no offline mode. Guide pages can be printed or saved through the browser's PDF dialog; the separate handwritten trip plan fits one A4 or Canadian Letter page in the tested Chromium output.

The 404 page uses the `/outdoorsafety/` project prefix so links and assets also work on nested missing URLs. Update that prefix if the publishing path changes.
