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
