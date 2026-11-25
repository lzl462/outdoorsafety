# Plan

Outdoor Safety — Sea-to-Sky. The live site is the current working copy:

https://lzl462.github.io/outdoorsafety/

Deadline: Monday 30 Nov 2026.

The name is still a stand-in. The current website includes the interview material. The content and structure baseline in section 7 is complete. Next: carry out a complete redesign. School and presentation deliverables continue alongside that work.

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
- Pages: Home, Before you leave, Shared essentials and activity notes, Be aware, Quick reminders, What to do if, No cell service, Emergency numbers, Common mistakes, About this project. `activities.html` and `pdfs.html` redirect to the Before you leave page (`checklists.html`).
- There is one printable, handwritten trip plan, `pdfs/before-you-leave.html`, linked from the Before you leave page. It includes the useful fields from the older leave-behind form. The hiking, biking, and climbing trip-plan variants were archived.
- Shared emergency essentials and hiking, biking, climbing and winter considerations are on `pack-lists.html`, built from existing lists in the repo, the 24 Nov 2026 backup zip and AdventureSmart. These are not complete technical sport-equipment checklists.
- A short No cell service page is on `no-service.html`.
- Be aware has two photo circles. The source line at the bottom is off the page. Liz asked to leave it off. Do not put it back unless she asks for an About page.
- Emergency numbers has the main table at the top, then other verified numbers. Empty story/photo rows were removed during the content baseline; the real hiking and biking examples belong on About.
- The cardboard plan is `pdfs/trifold.html`. The website QR is `images/qr-website.svg`.
- Every public page and print sheet has the shared disclaimer: “This is not an official rescue site. In an emergency, call 9-1-1.” The number is written 9-1-1, with hyphens, to match E-Comm 9-1-1.
- Publication, including a push to `main`, requires Liz's request. Repository-only changes do not count as completing a website-content task.
- GitHub Pages is published from the `main` branch, folder `/` (root), not from GitHub Actions. The README now says this.
- Leftover print sheets and `scripts/build_pdfs.py` are in `archive/`. The billing sentence “You will not be billed for Search and Rescue in British Columbia” was removed before those files were moved.

## 1. Website content

- [x] **Done** — Home uses Christine Strub’s genuine interview quote, with her name/role and a link to About. The old “What this website is for” text stays off the page.
- [x] **Done** — Removed the empty public hike/water story prompts from Emergency numbers (section 7, C8). The verified hiking case and anonymous rider account are on About. Any additional real story, including a water example, remains optional.
- [ ] **Liz** — Choose the real project name. Update Home, the sidebar, and the trifold title when it is chosen.
- [x] **Done** — One short page for when a phone has no service (`no-service.html`).
- [x] **Obsolete** — Make the hike, ride, and climb plans less alike. Replaced by one shared trip plan plus the Pack lists page.
- [ ] **Later** — Print/PDF feature (download key pages as PDF). The `pdfs/` folder was not renamed. Printing is postponed.
- [ ] **Later** — More pictures, quotes, and stories only when Liz has the real words and the photo has a name.
- [ ] **Later** — Clean up the image files at the end. Not before the content work in this plan is done. Be aware and What to do if embed large photos as base64, which is why those files are big.

- [x] **Done** — About this project (`about.html`) explains the capstone motivation, includes a sourced 2026 hiking case, the anonymous rider story and the contributions from both interviews, links to practical advice, and lists sources. Liz requested direct use on 25 Nov; the additional approval steps were removed. No claim of speaker review or organization endorsement is made.

## 2. Website technical

- [ ] **Ready** — Complete redesign following the completed content/structure baseline in section 7. Rework navigation, layouts and usability across phone, tablet and desktop, including the trip-plan destination. Native iOS/iPadOS acceptance remains open. A PWA is optional.
- [ ] **Later** — Independent review of the complete redesign, using the reader-task and device acceptance criteria in section 7. A no-overflow result alone does not establish usable navigation or task completion.
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

The practical advice lives on the existing pages. About explains the project and includes the anonymous mountain-biker account; section 7 adds the sourced hiking case. Public wording is maintained in `content.md`; the transcripts remain source material in `interviews/`.

### Sources

| Source | Use in the revision |
| --- | --- |
| [Christine Strub's written interview](interviews/christine-strub-squamish-sar.md), 27 Oct 2026 | Q5–6: the 3 T's, route judgement, elevation and turnaround. Q2 and Q7–10: calling, communication, trusted contacts, warmth, and personal equipment needs. Q12: the exact Home quote. |
| [Ms. Lejeune, 10:01](<interviews/Nov 5 at 10-01 AM_codex.md>) | 00:29: role. 01:43–04:25: the experienced rider's rescue and leaving a plan. 05:22–07:09: equipment, cold after stopping, and the time needed to reach someone. |
| [Ms. Lejeune, 10:10](<interviews/Nov 5 at 10-10 AM_codex.md>) | 00:03–03:03: experience, daylight, energy for the descent, unease and group dynamics. 03:03–06:24: calling, waiting and communication backup. The unresolved phrase is excluded. |
| [Ms. Lejeune, 10:18](<interviews/Nov 5 at 10-18 AM_codex.md>) | 00:18–02:14: the activity, season, talking to people and leaving a route/check-in plan. |
| [E-Comm](https://www.ecomm911.ca/911-dispatch/tips-and-info/) and [Squamish SAR](https://squamishsar.org/contact/) | Public calling guidance: call 9-1-1, explain the situation and location, answer questions and follow instructions. The site gives no police-versus-ambulance decision tree. |
| [AdventureSmart's 3 T's](https://www.adventuresmart.ca/the-three-ts/), [trip-plan guidance](https://www.adventuresmart.ca/trip-plan/) and [emergency communication](https://www.adventuresmart.ca/interactive/) | Shared essentials, training, a reliable contact, communication limits and staying put after attempting contact. |
| [Canadian Red Cross](https://cdn.redcross.ca/prodmedia/crc/azure/documents/first-aid-program-2025/cpr_learner_guide_en.pdf), [Avalanche Canada](https://avysavvy.avalanche.ca/en-ca/when-to-call-for-help), [Canadian Safe Boating Council](https://csbc.ca/cold-water/) and [Lifesaving Society](https://sauvetage.qc.ca/en/services/developpment/ladder-approach) | Checks for the short first-aid, avalanche and water-response passages. These passages link to fuller guidance and do not pretend to replace training. |

### Completed implementation

- [x] **Done — A1: One emergency instruction.** Updated lost/hurt advice and aligned Tips, No cell service, Emergency numbers and the trifold. The call taker determines the response through their questions; no agency-selection instructions or direct SAR number were added.
- [x] **Done — A2: Consistent location/group advice.** Removed the generic ridge/reception-seeking and sending-someone instructions. The pages now say to stay together in a safe place, with an exception for immediate danger and actual responder instructions. Sources: the interviews and AdventureSmart. No external approval step remains.
- [x] **Done — A3: Preparing for the wait.** Added `if.html#waiting-for-help`, linked from No cell service, Tips, and packing advice. It covers layers before becoming cold, sweat/wet clothing, shelter, volunteer travel and helicopter limits. No routine fire-lighting instruction was added.
- [x] **Done — B1: Useful preparation.** Before you leave now has the 3 T's, four practical planning checks, and the trusted contact's job. The existing trip-plan sheet remains the single printable, handwritten plan.
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
- [ ] **Later** — Additional real stories are optional. The empty Emergency numbers slots were removed in section 7. The hiking case and rider account are on About; no water story was invented.
- [ ] **Liz** — Choose the final project name. The implementation keeps the current stand-in name.

The interview-integration slice was published at `37eaea8` and the live files were verified against that commit. The broader content/structure review and its remaining work are tracked in section 7.

## 7. Content and structure first, complete redesign second

Agreed and implemented on 25 Nov 2026 at Liz's request, including commit and push. Step 1 is complete. The full visual redesign is the next separate implementation slice.

- [x] **Done** — Three independent agents reviewed safety/primary sources, information architecture/reader journeys, and editorial/interview evidence at `37eaea8`. The coordinator reconciled their findings against the repository, primary sources and selected live journeys. The initial review changed planning documents only; the approved implementation below then changed public copy and pages.
- [x] **Done — Step 1: content and structure baseline.** Public copy was written in `content.md` first, then applied to the ten pages. The audience, page jobs, safety qualifications, practical research links and printable-plan mode are settled. Two reviewers subsequently checked the revised safety and editorial passages and found no material remaining issue within their bounded checks.
- [ ] **Ready — Step 2: complete redesign.** Rework navigation, layouts, typography, visual hierarchy and shared components around the content and reader tasks below. Use the acceptance requirements before publishing the next slice.

### Settled audience and page jobs

The scope used for this approved pass is plain-English preparation for beginners/visitors taking Sea-to-Sky day trips, with short emergency orientation and links to specialist guidance. The site does not promise a complete climbing, avalanche, medical or marine rescue manual. A final project name is still Liz's choice and does not block the redesign.

| Reader's task | Main content | Settled role |
| --- | --- | --- |
| Start here | Home | Distinct urgent-help, preparation and learning routes; brief audience/region wording; Christine's genuine quote. |
| Prepare a trip | Before you leave; Shared essentials and activity notes; Be aware | Planning and the contact handoff; shared emergency equipment plus bounded activity considerations; conditions and turnaround decisions. |
| Get help | What to do if; No cell service; Emergency numbers | Situation index and role-specific actions, urgent no-signal instructions first, shared waiting advice, then decorative photos. Contact tables come first on Emergency numbers. |
| Learn about the project | About; Common mistakes; Quick reminders | Hiking and biking examples, interview contribution and sources on About; assumption/action examples on Common mistakes; short linked summaries on Quick reminders. |

Current URLs and scenario anchors are retained. Fuller explanations have one main home; contextual summaries link to them. Existing styling is retained for this content slice; navigation grouping and mobile visual hierarchy remain redesign work.

### Review findings resolved

P1 and P2 were review priorities, not a claim that every earlier sentence was wrong.

| Finding | Completed change and evidence |
| --- | --- |
| **P1 / C1 — Injury priorities** | Hurt now checks responsiveness and normal breathing, prioritizes life-saving care and immediate bleeding pressure, and qualifies movement restrictions. Linked the [Canadian Red Cross 2025 CPR guide](https://cdn.redcross.ca/prodmedia/crc/azure/documents/first-aid-program-2025/cpr_learner_guide_en.pdf), printed pp. 12–13. The card remains a short orientation. |
| **P1 / C2 — Water decisions and roles** | Separated falling in from helping from shore. Breathing control precedes a conditional safe exit; flotation/waiting remains when exit is unsafe. No universal swim-for-shore rule. Sources: [CSBC](https://csbc.ca/cold-water/) and [Lifesaving Society](https://sauvetage.qc.ca/en/services/developpment/ladder-approach). |
| **P2 / C3 — Avalanche scope** | Separated being caught from helping a buried companion. Completed spare/no-spare caller qualifications, including 10 m separation from transceiver searchers, and linked the [full Avalanche Canada reminder](https://avysavvy.avalanche.ca/en-ca/when-to-call-for-help). Immediate companion rescue remains the priority. |
| **P2 / C4 — Small safety instructions** | Dogs are explicitly leashed and prohibited-pet areas respected. Removed the carrier-specific RAPP shortcut while retaining the full number. Turnaround wording now says to turn around at the agreed time/point. [BC Parks](https://bcparks.ca/plan-your-trip/visit-responsibly/wildlife-safety/) supports the wildlife/number qualifications. |
| **P1 / C5 — Honest plan entry** | Before you leave labels the sheet as printable and handwritten before the click and explains the copy handed to a trusted contact. It has no digital form controls. Mobile sheet layout and actual A4/Letter acceptance remain below. |
| **P2 / C6 — Packing promise** | Home, navigation, page title and introduction now describe shared essentials plus activity considerations. No complete technical cycling/climbing kit or invented equipment is promised. |
| **P2 / C7 — Evidence and useful links** | Added dated wildlife/stream source notes; used [Parks Canada's mountain-stream guidance](https://parks.canada.ca/pn-np/ab/jasper/activ/passez-stay/arrierepays-backcountry/securite-safety) with general scope. Removed the unsupported local cliff quantifier. Before you leave links to BC Parks route/advisory tools, ECCC weather, DriveBC and Avalanche Canada beside the planning task. No live forecast is copied. |
| **P1 / C8 — Public placeholders** | Removed both empty story/photo rows from Emergency numbers. Kept real examples on About; an optional water story does not block completion. No image assets were deleted. |
| **P2 / C9 — Page jobs and ordering** | Home separates prepare/help/learn; What to do if has a situation index and uninterrupted urgent cards; No cell service starts with help now. Quick reminders remains secondary. Routes and anchors are preserved. |
| **P2 / C10 — Plain-English consistency** | Explained personal flotation device, avalanche transceiver/probe, companion rescue and emergency-alert terminology. Reader roles and cross-page summaries were aligned. The genuine quote and anonymous rider account remain faithful. |

### New leading example: the 2026 hiking case

- [x] **Done** — Added `about.html#hiker-story` ahead of the anonymous rider account, with links from Home and Common mistakes and practical links to turnaround/lost advice.
- Verified case: Stanislav Volo left via the Sea to Sky Gondola on 30 August 2026, spent five nights lost, called 9-1-1 on 1 September and met rescuers at a forest service road on 4 September. Sources: [CityNews, 4 September](https://vancouver.citynews.ca/2026/09/04/squamish-hiker-found-alive/) and [his CityNews interview, 7 September](https://vancouver.citynews.ca/2026/09/07/squamish-bc-missing-hiker-found-shares-story/).
- The reported later account includes ignored fog warnings and the important positive point that he left a trip plan with his wife, who called for help. Source: [Stacy Thomas / The Squamish Chief, authorized reprint](https://www.theregional.com/hiker-shares-about-his-six-days-lost-on-squamish-mountain/). The [official BCSARA interview](https://www.youtube.com/watch?v=j_dN2ElyQYM) is linked; its full video was not independently transcribed for this change.
- The lesson to stop, call early and stay put when safe is independently supported by [AdventureSmart](https://www.adventuresmart.ca/trip-plan/). The site does not claim that movement caused every search difficulty or recommend copying the eventual walk-out. It includes his reported movement/search-aircraft experience without adding survival techniques, clinical details, a search-cost figure or invented quotations.
- Detailed provenance and checked dates are in `content.md`. The named public news case is separate from Ms. Lejeune's anonymous biking account.

### Step 1 acceptance and limits

- Source/copy checks cover local links and anchors, consistent navigation, one main page heading, the shared disclaimer, genuine quote, and retained embedded image data. Public editing prompts and the unsupported local cliff claim are absent.
- Chrome checks covered all ten pages at 320/390/768/1440-pixel widths without horizontal overflow. Preparation/story/turnaround, printable-plan, urgent-help/no-signal/waiting and packing links were followed; all seven reminder accordions opened. The trip plan was checked as a printable sheet with no input controls, not certified as a usable mobile digital form.
- Native Safari/iOS/iPadOS, actual A4/Letter pagination, offline behaviour, phone/SOS networks and field/clinical validation remain outside these checks. A no-overflow result is not evidence that the current design is good. The school rubric is absent, so this is not a certification of every course deliverable.
- No extra speaker-approval gate, claim of organizational endorsement, billing claim or image-file cleanup was introduced. Git/SSH/credential configuration remains unchanged.

### Step 2 redesign brief and acceptance

- [ ] **Ready** — Create one coherent design around the reader tasks: navigation hierarchy, typography, spacing, page templates, contact/action components and responsive behaviour. Keep the school project's voice and real local material. Do not select a new framework or hosting service merely for appearance.
- [ ] **Ready** — Make urgent entry/actions visible and reachable on a small phone without scrolling past the full menu. At the pre-baseline review snapshot `37eaea8`, the 320 × 568 menu was about 382 pixels tall and the call box began about 618 pixels down; at 390 × 844 the call box began about 574 pixels down. A situation index is now present, but the shared visual layout still needs replacement.
- [ ] **Ready** — Rework the trip-plan destination for phone/tablet/desktop and actual A4/Canadian Letter output. The current fixed 210 mm screen sheet produced an approximately 810-pixel layout viewport and 794-pixel sheet in 390-pixel emulation. Retain a clear print/handwrite option. Evaluate [AdventureSmart's existing web plan](https://plan.adventuresmart.ca/) before proposing any additional phone-fillable/shareable local tool. Define what is saved/shared and what the trusted contact receives; this slice introduced no custom form/backend.
- [ ] **Ready** — Decide a practical save/print/offline strategy for emergency information. Do not promise the current online site works without a connection. A PWA is optional.
- [ ] **Ready** — Validate complete reader tasks on phone, tablet and desktop: keyboard access, focus/heading structure, contrast, readable text at zoom, slow loading, missing images, JavaScript unavailable and direct section links. Include actual Safari/iOS/iPadOS when available; distinguish it from emulation.
- [ ] **Ready** — Independently review the completed design and resolve material findings. Preserve old routes, anchors, contact links and printed QR destinations. Image-file cleanup can follow completed content work, but was deliberately not bundled into this slice.

## Next up

1. **Ready** — Review the completed content/structure baseline with Liz, then implement the complete redesign using section 7's reader tasks and functional/device acceptance requirements.
2. **Liz** — Continue the project name, portfolio, interviews and presentation tasks. Check the actual school rubric when it becomes available.
3. **Later** — General Print/PDF feature and image-file cleanup. The existing trip plan's responsive preview and A4/Letter behaviour belong in the redesign itself.

## Open questions

- Where is the official rubric or requirement checklist?
- Where does the portfolio live (Obsidian, a school portal, or somewhere else), and should this repository link to it?
- Are the remaining course interviews already scheduled?
- Thank-you notes: handwritten or email? Are there drafts?
- Is Instagram still in scope?
