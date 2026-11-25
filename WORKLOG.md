# Worklog

What changed, and why. This is not a copy of the plan.

## 2026-11-24

The Mac folder was an old September checkout. The website had moved on because single files were sent to GitHub. The folder was zipped to `/Users/liz/Projects/Backup/outdoorsafety-2026-11-24.zip`, then this repository was reset to GitHub `main` at `9cda134`. Reason: the live site is the working copy, and the old git history on the Mac did not match it. The extra photos and pack lists are only in the zip.

`PLAN.md`, `WORKLOG.md`, and `AGENTS.md` were added. Reason: the repository had page text, but no list of open work and no place to record why a change was made.

`AGENTS.md` now says the plan, the worklog, and this file stay in English. Reason: Liz will show the repository when she presents the project at school. Conversation with her can still be German or English.

`PLAN.md` was rewritten into five workstreams (Website content, Website technical, Capstone deliverables/school, Outreach, and Presentation/physical), with status tags, a short Next up list, and open questions. Reason: the earlier list mixed Liz-only writing, joint website work, school deliverables, and outreach, so the next step was hard to pick.

The capstone hand-in deadline, Monday 30 Nov 2026, was added near the top of `PLAN.md`, and the open question about the hand-in date was removed. Reason: the due date is now known.

The website QR item moved from Website technical to Presentation/physical, and the "QR on Home" step was dropped. Reason: the QR is for printed things (the trifold poster, flyers). People already on the site do not need it. `images/qr-website-print.svg` was added: a scalable SVG of the same QR (https://lzl462.github.io/outdoorsafety/), with a viewBox and high error correction, so it can be printed at any size. The older `images/qr-website.svg` stays, because `pdfs/trifold.html` uses it.

The shared safety disclaimer is now the same on every public page and print sheet: “This is not an official rescue site. In an emergency, call 9-1-1.” Reason: Liz asked for one consistent sentence, and whether 9-1-1 should have hyphens. E-Comm 9-1-1, the official B.C. 9-1-1 operator, writes 9-1-1 with hyphens, and the site already used that form in most places. “In an emergency,” was added so the line does not read as “call 9-1-1 instead of using this site.” The old variants (“Call 9-1-1.” and “If someone is in danger, call 9-1-1.”) were replaced. The sentence lives in `content.md` and is styled with `.site-disclaimer`. Form labels that said “Call 911” were changed to “Call 9-1-1.” Nothing was published.


The plan item about a photographer credit for the highway photo on What to do if was removed. Reason: Liz decided the photos will be replaced or generated at the end, so the credit is not needed for this school project.

`README.md` now says the live site is published from the `main` branch, from the root folder, not from GitHub Actions. Reason: the repo Pages setting is “Deploy from a branch” (`build_type: legacy`, branch `main`, path `/`). The extra workflow file `.github/workflows/pages.yml` still runs on push, but it is not the official publish method. Nothing was published.

The custom workflow `.github/workflows/pages.yml` was removed. Reason: the live site is published by GitHub's branch deploy from `main`. The extra workflow ran on every push, could race the branch deploy, and sometimes failed.

The banned sentence “You will not be billed for Search and Rescue in British Columbia” was removed from `pdfs/if-injured.html` and from `scripts/build_pdfs.py` before those files were archived. Reason: the project must not say that rescue in B.C. is free.

Useful lines from the old print sheets were moved onto the website. What to do if now includes asking for police and Search and Rescue, giving a phone GPS location, not walking downhill through bush to cliffs, what to tell the 9-1-1 operator, bleeding, a long wait and a helicopter signal, and sending someone to cell service only if 9-1-1 cannot connect. Emergency numbers gained a second table of other numbers, each checked against an official source. Clinic addresses were left off. A short No cell service page was added from wording already on Be aware, Tips, and the old if-lost and if-injured sheets. Pack lists is a new page, with hiking from the day-hike checklist and the hiking trip plan, winter from the winter checklist, and biking and climbing from the 24 Nov 2026 backup pack lists. The sidebar and the Home topics grid now include both new pages. The shared disclaimer is on the new pages too.

There is now one fill-in trip plan. Extra fields from the older leave-behind form were merged into `pdfs/before-you-leave.html`, and the duplicate date and people lines were removed. The Before you leave page links only that plan, and points people to Pack lists for gear. The hiking, biking, and climbing trip-plan sheets, the other leftover print sheets, and `scripts/build_pdfs.py` were moved to `archive/`. `pdfs/trifold.html` and `pdfs/trip-plan.css` stayed. The folder was not renamed, because printing is postponed.

`AGENTS.md` and `PLAN.md` now allow pack lists on the site when the items already exist in the repository or come from a verified source. The plan item to make the hike, ride, and climb plans less alike is marked obsolete. The no-service page and the leftover-files item are done. A Later item was added for a Print/PDF feature.


`interviews/` was added: Christine Strub's written interview answers (Squamish SAR, Oct 27 2026) as Markdown, and three audio recordings from Nov 5. Not linked from the site. Her phone number and postal address from the email signature were left out because the repository is public. Reason: keep the interview material with the project for the portfolio and later quotes.

## 2026-11-24 (evening)

An About page was added to the plan as a Liz item. Reason: Liz wants a page about the website. She decides its content.

The About page item now states its main focus: why the site matters and Liz's motivation (Sea-to-Sky capstone project, many 2026 incidents with unprepared people who were lucky).

A draft of the About page wording was added to `content.md` for Liz to review. Reason: Liz asked for the rest of the About content to be drafted from her note about why the page matters. The draft is not on the website yet.

A new plan section, “Website revision based on the interviews,” was added after comparing Christine Strub’s written answers and Ms. Lejeune’s three 5 Nov transcripts with the live site and `content.md`. Reason: Liz asked for a full comparison and a plan of pages to add, pages to change, text to add, and errors to fix. Site pages and `content.md` were not changed.
