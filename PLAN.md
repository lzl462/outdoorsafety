# Plan

Outdoor Safety — Sea-to-Sky. The live site is the current working copy:

https://lzl462.github.io/outdoorsafety/

The name is still a stand-in. One real quote, the interview notes, and the cardboard or Instagram move the project more than another design change.

## Rules

- Do not invent quotes, stories, or a gear list.
- Do not write that rescue in B.C. is free.
- Pack lists stay off the site. The older pack lists (`pdfs/pack-hiking.html`, `pdfs/pack-biking.html`, `pdfs/pack-climbing.html`) are only in the 24 Nov 2026 backup zip, not in this working copy. Do not restore them to the site.
- Do not publish until Liz asks.

## Status tags

- **Liz** — waiting on Liz’s writing, a decision, or a physical or account step.
- **Ready** — can be done without new writing from Liz. Still do not publish until she asks.
- **Blocked** — needs a Liz decision or artifact first.
- **Later** — after the content work above is done, or after something else exists.

## Done

- The website is on GitHub Pages.
- Pages: Home, Before you leave, Be aware, Tips, What to do if, Emergency numbers, Common mistakes. `activities.html` and `pdfs.html` redirect to the Before you leave page (`checklists.html`).
- Trip plans are online. The old “PDF later” placeholders are gone. The Before you leave page links four HTML print sheets: the general trip plan (`pdfs/before-you-leave.html`), hiking, biking, and climbing. Each has blank “For this trip, I need” lines. These are not full gear lists.
- Be aware has two photo circles. The source line at the bottom is off the page. Liz asked to leave it off. Do not put it back unless she asks for an About page.
- Emergency numbers has the table at the top, then two photo circles with an “Add a story” box beside each one. The boxes are still empty.
- The cardboard plan is `pdfs/trifold.html`. The website QR is `images/qr-website.svg`.
- Local branch `main` tracks `origin/main`.

## 1. Website content

- [ ] **Liz** — Home quote. The box on Home still says “add quote”. Liz writes the real quote. Do not invent one. The old “What this website is for” text is off the page.
- [ ] **Liz** — Two emergency stories. The boxes still say “Add a story.” One is a real hike, the other something real on the water. No names. Do not invent them.
- [ ] **Liz** — Choose the real project name. Update Home, the sidebar, and the trifold title when it is chosen.
- [ ] **Ready** — Make the hike, ride, and climb plans less alike, using lines already on the site.
- [ ] **Ready** — Add the line “This is not an official rescue site. Call 9-1-1.” on pages that do not have it. It is already on What to do if, Be aware, and most trip-plan sheets. It is missing on Home, Tips, Emergency numbers, Common mistakes, the Before you leave page, `pdfs/emergency-numbers.html`, and `pdfs/trip-plan.html`.
- [ ] **Ready** — One short page for when a phone has no service.
- [ ] **Ready** — Give the highway photo on What to do if a photographer name, or replace it. The credit now only says “Sea-to-Sky Highway and Howe Sound.”
- [ ] **Later** — More pictures, quotes, and stories only when Liz has the real words and the photo has a name.
- [ ] **Later** — Clean up the image files at the end. Not before the content work in this plan is done. Be aware and What to do if embed large photos as base64, which is why those files are big.

## 2. Website technical

- [ ] **Ready** — Put the website QR on Home.
- [ ] **Blocked** — Make the Instagram follow QR after the @ name exists, and put it beside the website QR.
- [ ] **Ready** — Confirm how GitHub Pages is actually deployed. The README says “Deploy from a branch” (`main`, folder `/ (root)`). The repo also has `.github/workflows/pages.yml` (GitHub Actions).
- [ ] **Ready** — Decide what to do with unlinked leftover files in `pdfs/`: `day-hike-checklist.html`, `winter-backcountry-checklist.html`, `if-lost.html`, `if-injured.html`, `emergency-numbers.html`, and `trip-plan.html` (plus `trip-plan.css`). Keep, archive, or remove. Do not put pack lists on the site.

## 3. Capstone deliverables / school

- [ ] **Liz** — Listen to Ms. Lejeune’s audios. Write three notes, in her own words, on an Interview page in the portfolio.
- [ ] **Liz** — Do the interviews that are still part of the course.
- [ ] **Liz** — Finish the portfolio. The portfolio files are not in this repository. `content.md` mentions Obsidian `Website-Inhalte` as one place for new wording.
- The hand-in date and the official rubric are not in this repository. See Open questions.

## 4. Outreach

- [ ] **Liz** — Thank-you note to Christine Strub and Ms. Lejeune.
- [ ] **Liz** — Create the Instagram account and send the @ name. Liz creates the account herself. Draft name: Outdoor Safety — Sea-to-Sky. Draft bio: Simple tips, in our own words. Not an official rescue site. Link: https://lzl462.github.io/outdoorsafety/
- [ ] **Blocked** — Write the Instagram posts after the account exists.
- [ ] **Later** — Ask someone from search and rescue to look at the live pages.

## 5. Presentation / physical

- [ ] **Liz** — Build the cardboard from `pdfs/trifold.html`. The big title can change when the project name is chosen.

## Next up

1. **Ready** — Add the official-rescue line to the pages that do not have it. Do not publish until Liz asks.
2. **Ready** — Put the website QR on Home. Do not publish until Liz asks.
3. **Liz** — Write the Home quote, the two emergency stories, and/or choose the project name. These unblock most of the public-facing work.

## Open questions

- What is the hand-in or presentation date?
- Where is the official rubric or requirement checklist?
- Where does the portfolio live (Obsidian, a school portal, or somewhere else), and should this repository link to it?
- Are the remaining course interviews already scheduled?
- Thank-you notes: handwritten or email? Are there drafts?
- Is Instagram still in scope?
- Who should do the search-and-rescue review?
- Which GitHub Pages method is actually live (branch deploy or Actions)?
- Should the unlinked leftover files in `pdfs/` be removed from `main`?
