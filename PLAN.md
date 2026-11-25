# Plan

Outdoor Safety — Sea-to-Sky. The live site is the current working copy:

https://lzl462.github.io/outdoorsafety/

Deadline: Monday 30 Nov 2026.

The name is still a stand-in. One real quote, the interview notes, and the cardboard or Instagram move the project more than another design change.

## Rules

- Do not invent quotes or stories.
- Do not write that rescue in B.C. is free.
- Pack lists are allowed on the site. Build them only from lists already in the repository or from verified sources. Do not invent items.
- Do not publish until Liz asks.

## Status tags

- **Liz** — waiting on Liz’s writing, a decision, or a physical or account step.
- **Ready** — can be done without new writing from Liz. Still do not publish until she asks.
- **Blocked** — needs a Liz decision or artifact first.
- **Later** — after the content work above is done, or after something else exists.

## Done

- The website is on GitHub Pages.
- Pages: Home, Before you leave, Pack lists, Be aware, Tips, What to do if, No cell service, Emergency numbers, Common mistakes. `activities.html` and `pdfs.html` redirect to the Before you leave page (`checklists.html`).
- There is one fill-in trip plan, `pdfs/before-you-leave.html`, linked from the Before you leave page. It includes the useful fields from the older leave-behind form. The hiking, biking, and climbing trip-plan variants were archived.
- Pack lists are on `pack-lists.html`: hiking, biking, climbing, and winter, built from existing lists in the repo and from the 24 Nov 2026 backup zip.
- A short No cell service page is on `no-service.html`.
- Be aware has two photo circles. The source line at the bottom is off the page. Liz asked to leave it off. Do not put it back unless she asks for an About page.
- Emergency numbers has the main table at the top, then other verified numbers, then two photo circles with an “Add a story” box beside each one. The boxes are still empty.
- The cardboard plan is `pdfs/trifold.html`. The website QR is `images/qr-website.svg`.
- Every public page and print sheet has the shared disclaimer: “This is not an official rescue site. In an emergency, call 9-1-1.” The number is written 9-1-1, with hyphens, to match E-Comm 9-1-1.
- Local branch `main` is ahead of `origin/main`. Do not push until Liz asks.
- GitHub Pages is published from the `main` branch, folder `/` (root), not from GitHub Actions. The README now says this.
- Leftover print sheets and `scripts/build_pdfs.py` are in `archive/`. The billing sentence “You will not be billed for Search and Rescue in British Columbia” was removed before those files were moved.

## 1. Website content

- [ ] **Liz** — Home quote. The box on Home still says “add quote”. Liz writes the real quote. Do not invent one. The old “What this website is for” text is off the page.
- [ ] **Liz** — Two emergency stories. The boxes still say “Add a story.” One is a real hike, the other something real on the water. No names. Do not invent them.
- [ ] **Liz** — Choose the real project name. Update Home, the sidebar, and the trifold title when it is chosen.
- [x] **Done** — One short page for when a phone has no service (`no-service.html`).
- [x] **Obsolete** — Make the hike, ride, and climb plans less alike. Replaced by one shared trip plan plus the Pack lists page.
- [ ] **Later** — Print/PDF feature (download key pages as PDF). The `pdfs/` folder was not renamed. Printing is postponed.
- [ ] **Later** — More pictures, quotes, and stories only when Liz has the real words and the photo has a name.
- [ ] **Later** — Clean up the image files at the end. Not before the content work in this plan is done. Be aware and What to do if embed large photos as base64, which is why those files are big.

## 2. Website technical

- [ ] **Ready** — Responsive, mobile-first design. The site must work well and adapt automatically on iOS devices from iPhone to iPad, and in normal desktop browsers. A PWA is optional.
- [ ] **Later** — Independent design review once the site structure is finished. Check that the whole design is modern, uses current web features, and is genuinely good: inviting but clear, and cool.
- [ ] **Blocked** — Make the Instagram follow QR after the @ name exists, and put it beside the website QR.
- [x] **Done** — Leftover print sheets were archived to `archive/pdfs/`. `trip-plan.css` stays in `pdfs/` because the live trip plan uses it. `scripts/build_pdfs.py` was retired to `archive/scripts/`.

## 3. Capstone deliverables / school

- [ ] **Liz** — Listen to Ms. Lejeune’s audios. Write three notes, in her own words, on an Interview page in the portfolio.
- [ ] **Liz** — Do the interviews that are still part of the course.
- [ ] **Liz** — Finish the portfolio. The portfolio files are not in this repository. `content.md` mentions Obsidian `Website-Inhalte` as one place for new wording.
- The official rubric is not in this repository. See Open questions.

## 4. Outreach

- [ ] **Liz** — Thank-you note to Christine Strub and Ms. Lejeune.
- [ ] **Liz** — Create the Instagram account and send the @ name. Liz creates the account herself. Draft name: Outdoor Safety — Sea-to-Sky. Draft bio: Simple tips, in our own words. Not an official rescue site. Link: https://lzl462.github.io/outdoorsafety/
- [ ] **Blocked** — Write the Instagram posts after the account exists.
- [ ] **Later** — Ask someone from search and rescue to look at the live pages.

## 5. Presentation / physical

- [ ] **Liz** — Build the cardboard from `pdfs/trifold.html`. The big title can change when the project name is chosen.
- [ ] **Liz** — Print the website QR for the trifold poster and any flyer. Print file: `images/qr-website-print.svg` (scalable, points to https://lzl462.github.io/outdoorsafety/). Make a new one if the site address changes. The QR is not needed on the website itself.

## Next up

1. **Liz** — Write the Home quote, the two emergency stories, and/or choose the project name. These unblock most of the public-facing work.
2. **Ready** — Responsive, mobile-first design so the site adapts automatically on iPhone, iPad, and desktop.
3. **Later** — Independent design review once the site structure is finished.
4. **Later** — Print/PDF feature (download key pages as PDF), after the remaining Liz writing is in.

## Open questions

- Where is the official rubric or requirement checklist?
- Where does the portfolio live (Obsidian, a school portal, or somewhere else), and should this repository link to it?
- Are the remaining course interviews already scheduled?
- Thank-you notes: handwritten or email? Are there drafts?
- Is Instagram still in scope?
- Who should do the search-and-rescue review?
