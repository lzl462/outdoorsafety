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
- Pages: Home, Before you leave, Pack lists, Be aware, Tips, What to do if, No cell service, Emergency numbers, Common mistakes, About this project. `activities.html` and `pdfs.html` redirect to the Before you leave page (`checklists.html`).
- There is one fill-in trip plan, `pdfs/before-you-leave.html`, linked from the Before you leave page. It includes the useful fields from the older leave-behind form. The hiking, biking, and climbing trip-plan variants were archived.
- Pack lists are on `pack-lists.html`: hiking, biking, climbing, and winter, built from existing lists in the repo and from the 24 Nov 2026 backup zip.
- A short No cell service page is on `no-service.html`.
- Be aware has two photo circles. The source line at the bottom is off the page. Liz asked to leave it off. Do not put it back unless she asks for an About page.
- Emergency numbers has the main table at the top, then other verified numbers, then two photo circles with an “Add a story” box beside each one. The boxes are still empty.
- The cardboard plan is `pdfs/trifold.html`. The website QR is `images/qr-website.svg`.
- Every public page and print sheet has the shared disclaimer: “This is not an official rescue site. In an emergency, call 9-1-1.” The number is written 9-1-1, with hyphens, to match E-Comm 9-1-1.
- Publication, including a push to `main`, requires Liz's request. Repository-only changes do not count as completing a website-content task.
- GitHub Pages is published from the `main` branch, folder `/` (root), not from GitHub Actions. The README now says this.
- Leftover print sheets and `scripts/build_pdfs.py` are in `archive/`. The billing sentence “You will not be billed for Search and Rescue in British Columbia” was removed before those files were moved.

## 1. Website content

- [x] **Done** — Home uses Christine Strub’s genuine interview quote, with her name/role and a link to About. The old “What this website is for” text stays off the page.
- [ ] **Liz** — Two emergency stories. The boxes still say “Add a story.” One is a real hike, the other something real on the water. No names. Do not invent them.
- [ ] **Liz** — Choose the real project name. Update Home, the sidebar, and the trifold title when it is chosen.
- [x] **Done** — One short page for when a phone has no service (`no-service.html`).
- [x] **Obsolete** — Make the hike, ride, and climb plans less alike. Replaced by one shared trip plan plus the Pack lists page.
- [ ] **Later** — Print/PDF feature (download key pages as PDF). The `pdfs/` folder was not renamed. Printing is postponed.
- [ ] **Later** — More pictures, quotes, and stories only when Liz has the real words and the photo has a name.
- [ ] **Later** — Clean up the image files at the end. Not before the content work in this plan is done. Be aware and What to do if embed large photos as base64, which is why those files are big.

- [x] **Done** — About this project (`about.html`) explains the capstone motivation, includes the anonymous rider story and the contributions from both interviews, links to practical advice, and lists sources. Liz requested direct use on 25 Nov; the additional approval steps were removed. No claim of speaker review or organization endorsement is made.

## 2. Website technical

- [ ] **Ready** — Responsive, mobile-first design. The site must work well and adapt automatically on iOS devices from iPhone to iPad, and in normal desktop browsers. A PWA is optional.
- [ ] **Later** — Independent design review once the site structure is finished. Check that the whole design is modern, uses current web features, and is genuinely good: inviting but clear, and cool.
- [ ] **Blocked** — Make the Instagram follow QR after the @ name exists, and put it beside the website QR.
- [x] **Done** — Leftover print sheets were archived to `archive/pdfs/`. `trip-plan.css` stays in `pdfs/` because the live trip plan uses it. `scripts/build_pdfs.py` was retired to `archive/scripts/`.

## 3. Capstone deliverables / school

- [x] **Done** — Independently transcribed the three Nov 5 recordings into `interviews/*_codex.md`, with timestamps and an explicit marker for unresolved speech. The original audio and earlier transcripts remain for comparison. These are working transcripts, not speaker-reviewed quotations.
- [ ] **Liz** — Listen to Ms. Lejeune’s audios. Write three notes, in her own words, on an Interview page in the portfolio.
- [ ] **Liz** — Do the interviews that are still part of the course.
- [ ] **Liz** — Finish the portfolio. The portfolio files are not in this repository. `content.md` mentions Obsidian `Website-Inhalte` as one place for new wording.
- The official rubric is not in this repository. See Open questions.

## 4. Outreach

- [ ] **Liz** — Thank-you note to Christine Strub and Ms. Lejeune.
- [ ] **Liz** — Create the Instagram account and send the @ name. Liz creates the account herself. Draft name: Outdoor Safety — Sea-to-Sky. Draft bio: Simple tips, in our own words. Not an official rescue site. Link: https://lzl462.github.io/outdoorsafety/
- [ ] **Blocked** — Write the Instagram posts after the account exists.
- [ ] **Later** — Optional feedback from local search and rescue, if useful for the project. This is not a prerequisite for the implementation/publication Liz requested.

## 5. Presentation / physical

- [ ] **Liz** — Build the cardboard from `pdfs/trifold.html`. The big title can change when the project name is chosen.
- [ ] **Liz** — Print the website QR for the trifold poster and any flyer. Print file: `images/qr-website-print.svg` (scalable, points to https://lzl462.github.io/outdoorsafety/). Make a new one if the site address changes. The QR is not needed on the website itself.

## 6. Website revision based on the interviews

Implemented on 25 Nov 2026 at Liz's request, including the request to commit and push. Liz removed the additional approval steps for this school project and asked for direct implementation. The website does not claim that the interviewees reviewed or endorsed the finished pages.

The practical advice lives on the existing pages. About explains the project and includes the anonymous mountain-biker account. Public wording is maintained in `content.md`; the transcripts remain source material in `interviews/`.

### Sources

| Source | Use in the revision |
| --- | --- |
| [Christine Strub's written interview](interviews/christine-strub-squamish-sar.md), 27 Oct 2026 | Q5–6: the 3 T's, route judgement, elevation and turnaround. Q2 and Q7–10: calling, communication, trusted contacts, warmth, and personal equipment needs. Q12: the exact Home quote. |
| [Ms. Lejeune, 10:01](<interviews/Nov 5 at 10-01 AM_codex.md>) | 00:29: role. 01:43–04:25: the experienced rider's rescue and leaving a plan. 05:22–07:09: equipment, cold after stopping, and the time needed to reach someone. |
| [Ms. Lejeune, 10:10](<interviews/Nov 5 at 10-10 AM_codex.md>) | 00:03–03:03: experience, daylight, energy for the descent, unease and group dynamics. 03:03–06:24: calling, waiting and communication backup. The unresolved phrase is excluded. |
| [Ms. Lejeune, 10:18](<interviews/Nov 5 at 10-18 AM_codex.md>) | 00:18–02:14: the activity, season, talking to people and leaving a route/check-in plan. |
| [E-Comm](https://www.ecomm911.ca/911-dispatch/tips-and-info/) and [Squamish SAR](https://squamishsar.org/contact/) | Public calling guidance: call 9-1-1, explain the situation and location, answer questions and follow instructions. The site gives no police-versus-ambulance decision tree. |
| [AdventureSmart's 3 T's](https://www.adventuresmart.ca/the-three-ts/), [trip-plan guidance](https://www.adventuresmart.ca/trip-plan/) and [emergency communication](https://www.adventuresmart.ca/interactive/) | Shared essentials, training, a reliable contact, communication limits and staying put after attempting contact. |
| [Canadian Red Cross](https://www.redcross.ca/crc/pdf/First-Aid-and-CPR-2017_digital.pdf), [Avalanche Canada](https://avysavvy.avalanche.ca/en-ca/when-to-call-for-help), [Canadian Safe Boating Council](https://csbc.ca/cold-water/) and [Lifesaving Society](https://sauvetage.qc.ca/en/services/developpment/ladder-approach) | Checks for the short first-aid, avalanche and water-response passages. These passages link to fuller guidance and do not pretend to replace training. |

### Completed implementation

- [x] **Done — A1: One emergency instruction.** Updated lost/hurt advice and aligned Tips, No cell service, Emergency numbers and the trifold. The call taker determines the response through their questions; no agency-selection instructions or direct SAR number were added.
- [x] **Done — A2: Consistent location/group advice.** Removed the generic ridge/reception-seeking and sending-someone instructions. The pages now say to stay together in a safe place, with an exception for immediate danger and actual responder instructions. Sources: the interviews and AdventureSmart. No external approval step remains.
- [x] **Done — A3: Preparing for the wait.** Added `if.html#waiting-for-help`, linked from No cell service, Tips, and packing advice. It covers layers before becoming cold, sweat/wet clothing, shelter, volunteer travel and helicopter limits. No routine fire-lighting instruction was added.
- [x] **Done — B1: Useful preparation.** Before you leave now has the 3 T's, four practical planning checks, and the trusted contact's job. The existing trip-plan form remains the single fill-in form.
- [x] **Done — B2: Shared packing baseline.** One visible essentials list now applies across hiking, biking, climbing and winter, followed by activity notes. Personal medication and spare glasses/contacts are included where needed. Avalanche equipment is labelled for avalanche terrain. No fixed water quantity is presented as sufficient for every trip, and no power bank was inferred from “Power bar”.
- [x] **Done — B3: Turning around.** Be aware now includes elevation, activity/season-specific experience, return energy, time/progress, unease and group pressure, with `#turn-around` as the main destination for links.
- [x] **Done — B4: Concrete common mistakes.** Replaced three general warnings with five assumption/action pairs and links to the main practical pages. The tone emphasizes preparation rather than blaming people who need help.
- [x] **Done — B5: Communication planning.** No cell service distinguishes offline navigation from sending an SOS, explains planning a suitable backup, and keeps the trusted contact as another layer of preparation. No product brand or successful-contact guarantee is required.
- [x] **Done — C1: Rider example on About.** Added the short account beside the project motivation with a link to the trip plan. The rider is unnamed, with no medical/recovery details, exact location or invented outcome. It is identified as Ms. Lejeune's interview account, not Liz's own experience. It does not claim that a trip plan would have prevented the fall.
- [x] **Done — C2: Local interview contributions.** About introduces both contributors with their recorded roles and dates, gives four lessons linked to practical pages, and lists public sources. The removed Be aware source footer was not restored.
- [x] **Done — C3: Home and navigation.** Home uses Christine's exact Q12 quote with attribution and a link to About. About appears in the Home topics and shared navigation. Active navigation is also identified for assistive technology.
- [x] **Done — D1: Source and copy consistency.** Updated `content.md` first, retained the genuine quote, excluded the uncertain audio phrase and unsupported 2026 incident-rate claims, and preserved existing image data/credits. No new gear, personal story or billing statement was invented.
- [x] **Done — D2: Specialist source checks.** Simplified the short response cards against the official sources above. In particular, companion rescue is urgent; an outside call must not interrupt it when there is no spare rescuer. This is a source check, not a claim of professional sign-off.
- [x] **Done — D3: Local acceptance.** Checked all ten pages at widths of 320, 390, 768 and 1440 pixels in Chrome with no horizontal overflow. Inspected About on desktop/mobile and What to do if on mobile, checked all seven Tips accordions, and followed the About-to-trip-plan link. Local links/anchors, one page heading, active navigation and the shared disclaimer passed checks. Native Safari/iOS was not tested.

### Deliberately separate work

- [ ] **Later** — A dedicated local-SAR/interview page only if additional material gives it a distinct purpose. About is the home for this revision's story and interview context.
- [ ] **Liz** — The two existing hike/water story slots on Emergency numbers still need real stories. The rider's account is on About and does not stand in for a water story.
- [ ] **Liz** — Choose the final project name. The implementation keeps the current stand-in name.

The interview-content implementation is complete. Publication was requested in this turn; verify the remote revision and deployed pages after the push.

## Next up

1. **Liz** — Choose the final project name and finish the remaining real hike/water stories, portfolio work and presentation deliverables.
2. **Ready** — Further responsive-design work and native iOS/iPadOS acceptance. This revision passed Chrome checks from 320 to 1440 pixels; that does not replace testing on actual Apple devices.
3. **Later** — Independent design review once Liz is happy with the remaining content.
4. **Later** — Print/PDF feature after the remaining personal writing is in.

## Open questions

- Where is the official rubric or requirement checklist?
- Where does the portfolio live (Obsidian, a school portal, or somewhere else), and should this repository link to it?
- Are the remaining course interviews already scheduled?
- Thank-you notes: handwritten or email? Are there drafts?
- Is Instagram still in scope?
