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
- Publication, including a push to `main`, requires Liz's request. Repository-only changes do not count as completing a website-content task.
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

- [ ] **Liz** — About page: one new page about the website itself. Main focus (Liz, Nov 24): why the site matters and what made Liz start this Sea-to-Sky school capstone project. Keep any 2026 incident statistics and claims about unpreparedness separately sourced; the interviews do not establish those wider claims. Liz suggested the experienced mountain biker's story on Nov 25 as a short example beside the project motivation. Include it only after Ms. Lejeune has approved that use and reviewed the wording; see section 6, C1. Add a small section on what the interviews contributed, verified contributor roles, the sources (the Be aware source line can return here), and the unofficial-site disclaimer. Drafts are in `content.md`. Liz's final content review and the relevant speaker permissions remain open.

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
- [ ] **Liz** — Arrange the safety-text review Christine has already offered, using the concrete drafts before publication, and request Ms. Lejeune's permission/review for her story and attribution. See section 6, A2 and D2. A review of selected passages is not an endorsement of the whole site.

## 5. Presentation / physical

- [ ] **Liz** — Build the cardboard from `pdfs/trifold.html`. The big title can change when the project name is chosen.
- [ ] **Liz** — Print the website QR for the trifold poster and any flyer. Print file: `images/qr-website-print.svg` (scalable, points to https://lzl462.github.io/outdoorsafety/). Make a new one if the site address changes. The QR is not needed on the website itself.

## 6. Website revision based on the interviews

Reviewed and rewritten on 25 Nov 2026 against the nine current site pages, the shared trip plan, `content.md`, Christine's written answers, and the three Codex transcripts. This is a content plan, not a completed website revision. Draft passages are in `content.md`, under “Interview-based revision drafts — 25 Nov 2026”. The HTML and CSS have not been changed by this review.

**Agreed direction:** improve the existing practical pages and use the planned About page to explain the project through the interviews. Liz suggested the mountain-biker story for About. Liz also decided that the site should tell people to call 9-1-1 and follow the call taker's instructions, without giving them a police-versus-ambulance decision tree.

### Sources and permission

The source labels below are for this plan, not for the public navigation.

| Source | Evidence to use |
| --- | --- |
| **C** — [Christine Strub's written interview](interviews/christine-strub-squamish-sar.md), 27 Oct 2026 | Q1: role. Q2: waiting and helicopter limits. Q3–4: research, risk, and the belief that an incident cannot happen to you. Q5: the 3 T's and planning. Q6: elevation, route judgement, and turnaround points. Q7–9: calling, keeping the group together, warmth, communication, and a reliable check-in person. Q10: essentials and personal needs. Q12: possible Home quote. |
| **L1** — [5 Nov, 10:01](<interviews/Nov 5 at 10-01 AM_codex.md>) | 00:29: role and winter team. 01:43–04:25: the rider's rescue and the lesson about leaving a plan. 04:25: unpreparedness and problems adding up. 05:22: gear suggestions. 06:03–07:09: cold after stopping and why rescue takes time. |
| **L2** — [5 Nov, 10:10](<interviews/Nov 5 at 10-10 AM_codex.md>) | 00:03–01:18: experience and learning from others. 01:18–03:03: daylight, energy for the descent, gut feeling, and group dynamics. 03:03–05:06: 9-1-1, remote guidance, and staying warm while awaiting instructions. 05:06–06:24: communication backup and anticipating needs while waiting. |
| **L3** — [5 Nov, 10:18](<interviews/Nov 5 at 10-18 AM_codex.md>) | 00:18–01:20: skill in the particular activity, season, weather, and gear. 01:20–02:14: talk to people, go beyond social-media pictures, and leave a plan with an expected return time. |
| **Official calling guidance**, checked 25 Nov | [E-Comm tips](https://www.ecomm911.ca/911-dispatch/tips-and-info/) and [Squamish SAR emergency contact](https://squamishsar.org/contact/). Use these to check public emergency wording; the interviews do not replace current operational guidance. |
| **Official preparation guidance**, checked 25 Nov | AdventureSmart: [the 3 T's and essentials](https://www.adventuresmart.ca/the-three-ts/), [Survive Outside](https://www.adventuresmart.ca/programs/survive-outside/), and [trip planning and the check-in person's role](https://www.adventuresmart.ca/trip-planning-where-every-adventure-starts-and-ends/). |
| **Fire advice boundary**, checked 25 Nov | [BC Wildfire Service campfire guidance](https://blog.gov.bc.ca/bcwildfire/open-burning-101-category-1-campfires/). A suggestion in an interview must not become a general instruction to light a fire. |

Christine is Prevention Team Coordinator with Squamish SAR. Her written permission covers quoting her answers with her name and role on the website and Instagram, with review before publication. She has also offered to review the safety information. Ms. Lejeune identifies herself in L1 as a regular Squamish SAR member specializing in rope and winter rescue and coordinating the winter team. Permission to publish her quotations or stories is not recorded; obtain it and let her review the proposed use. Do not describe either interview as an endorsement of the whole site.

The Codex files are working transcripts, not speaker-approved records. The older unsuffixed files remain for comparison; use the Codex timestamps for this plan. One short phrase in L2's gut-feeling passage remains `[unclear]`. It is not needed for the proposed advice. Do not publish full recordings or transcripts as a website feature without a separate decision and permission.

### What the review changes

- Keep the useful interview themes, but give each one a main home. The earlier plan repeated the same additions across several pages and did not make clear which pages already covered them.
- Add the missing decisions behind the equipment: training, an honest assessment of the group, an actual turnaround point, and an agreed check-in arrangement. The trip-plan form already has route, return, turnaround, contact, and alarm-time fields; another form would duplicate it.
- Treat the 9-1-1 change as one consistent site-wide wording decision. Squamish SAR's current contact page distinguishes lost/stranded people from injuries, supporting the concern about the existing hurt card. E-Comm asks callers questions and connects the appropriate service. Liz's chosen wording avoids making visitors classify the response themselves. Do not add an internal dispatch flowchart.
- Review movement and separation advice as well as the call wording. `no-service.html` suggests a nearby ridge and sending someone for reception; `if.html` also suggests sending someone. Those instructions need to be reconciled with the interviews' stay-together/stay-put guidance and the existing exception for an unsafe location. An unconnected call alone is not enough to decide that moving or splitting up is safe.
- Keep the full preparation baseline. L1 calls four items a minimum, then suggests further items; that short spoken answer is not a complete official packing standard. Use the verified AdventureSmart baseline across activities, with the speakers' additions identified accurately.
- Use the recovered group-dynamics passage now; it no longer needs deferring because of the earlier transcript's gap. The clear gut-feeling advice can also be paraphrased without completing the uncertain phrase.
- Make the benefit of preparation clear without blaming people who need help. Experience does not prevent every incident; preparation can reduce its consequences. Neither the rider's story nor a checklist proves that a rescue would have been avoided.

### Main home for each topic

| Page | Its job after revision | What changes from the current page |
| --- | --- | --- |
| Before you leave (`checklists.html`) | Help the reader make a realistic plan before filling in the form. | Add a compact 3 T's introduction, four practical checks, and a short explanation of the trusted contact's job. Keep the existing trip-plan and pack-list links prominent. |
| Pack lists (`pack-lists.html`) | Show the shared emergency basics, then what changes with the activity. | Make one visible common baseline available to hikers, riders, climbers, and winter users. Current biking/climbing lists lack some basics included under Hiking; Winter currently shows specialist advice without that shared baseline. |
| Be aware (`be-aware.html`) | Explain the local risks and when to change or abandon a plan. | Extend the existing trip/group and daylight sections with elevation, seasonal skill, the descent, and a compact turnaround panel. Keep the other established risk sections. |
| What to do if (`if.html`) | Give immediate actions when something has gone wrong. | Apply the agreed call instruction, resolve movement/separation advice, and add a short waiting-for-help block after the immediate lost/hurt steps. |
| No cell service (`no-service.html`) | Explain the communication backup and the limits of a phone. | Clarify planning versus actions during an emergency, link to waiting advice, and resolve the ridge/group-splitting instructions before publication. |
| Common mistakes (`mistakes.html`) | Turn common assumptions into specific better choices. | Replace the three general admonitions with a small set of mistake/action pairs linking to the fuller instructions. |
| Tips (`tips.html`) | Give short reminders and routes into the main instructions. | Update summaries and add links; do not make it another full interview-advice page. Urgent call steps should be visible without opening an accordion. |
| About (planned) and Home (`index.html`) | Explain why Liz made the project and show what the local interviews contributed. | About gets the short rider example and interview context. Home may get one approved real quote and a link to About. |
| Emergency numbers (`emergency.html`) | Keep the emergency number and other contacts easy to find. | Align its short calling explanation. Avoid a second detailed rescue guide or interview article above the numbers. The existing hike/water story slots remain a separate Liz decision. |

### A. First: emergency consistency

- [ ] **Ready** — **A1: One call instruction.** Use the prepared draft in `content.md` for both lost and hurt situations; align Tips, Emergency numbers, No cell service, and any corresponding print wording. Keep the current useful list of information to give the call taker. Do not add a SAR direct number, fixed response time, or agency-selection rule. Sources: C Q7–9, L2 03:03–05:06, E-Comm. Draft exists; HTML integration is still open.
- [ ] **Blocked** — **A2: Resolve movement and group separation with a qualified reviewer.** Review the exact ridge, moving, and sending-someone lines in `no-service.html`, `if.html`, and their `content.md` counterparts. Keep the immediate-danger exception and follow actual responder instructions when available. Do not simply replace one unconditional rule with another. Christine has offered a review; Liz can arrange it. Sources: C Q7–9 and L2 04:24–05:06. Resolution is required before the affected emergency passages are approved for publication.
- [ ] **Ready** — **A3: Prepare for the wait.** Put the concise waiting block on `if.html`; link to it from No cell service and Tips. Explain cold after stopping, wet clothing from sweat, volunteer mobilization/travel, and helicopter limits. Keep this after the urgent actions. Do not turn L2's possible fire suggestion into standard instructions; leave fire-making advice out of the short action block pending qualified review of conditions and restrictions. Sources: C Q2 and Q9, L1 06:03–07:09, L2 05:54–06:24.

### B. Next: practical preparation on the existing pages

- [ ] **Ready** — **B1: Planning that changes a decision.** On Before you leave, explain Trip Planning, Training, and Taking the Essentials in plain English and link to AdventureSmart. Use the four checks drafted in `content.md`: route/group fit, turnaround conditions and time, a trusted contact and agreed alarm time, and equipment/communication for a delayed return. Cover elevation, mountain weather, exposure, water planning, access and the return journey. Explain that the contact keeps the plan and calls 9-1-1 if the agreed return/check-in arrangement is missed. Do not invent a mandatory waiting period. Equipment should be accompanied by the knowledge to use it. Sources: C Q5–6 and Q9, L1 03:00, L2 00:03–01:18, L3 00:18–02:14, AdventureSmart. Changing the printable form remains Liz's choice; the existing fields cover the core handoff.
- [ ] **Ready** — **B2: One shared pack baseline.** On Pack lists, use the verified essentials already present in the hiking material and AdventureSmart: light, fire-making kit, signalling, extra food/water, clothing, navigation/communication, first aid, shelter, knife, and sun protection. Make their relevance to all activities clear before the activity sections. Add personal medication and spare glasses/contacts where needed, from C Q10. Preserve the distinction between common emergency basics and specialist climbing/avalanche equipment; these interviews do not certify a complete climbing or winter kit. The winter avalanche-equipment advice should be labelled for avalanche terrain rather than presented as a requirement for every winter outing. Sources: C Q5 and Q10, L1 05:22, L3 00:18–01:20, current repository lists, AdventureSmart. Do not reinterpret Christine's ambiguous “Power bar” as a power bank without asking her; the existing food advice stands independently. Do not present one water quantity as sufficient for every route or season.
- [ ] **Ready** — **B3: A useful turnaround panel.** Extend Be aware's existing group-fit/daylight advice rather than creating a new page. Cover distance plus elevation, activity-specific and seasonal experience, a pre-agreed time/point, remaining daylight and progress, enough energy for descent, unease, and group pressure. Sources: C Q6, L2 00:03–03:03, L3 00:18. Use a short summary/link in Tips. The uncertain L2 phrase is excluded. Do not suggest that feeling confident establishes safety.
- [ ] **Ready** — **B4: Specific mistakes, specific alternatives.** Rework Common mistakes into about five short pairs: treating a photo or an “easy” comment as route research; reading distance without elevation; continuing because the destination is close; packing only for warmth while moving; and believing familiarity or experience removes the need for a plan. Give each a clear action and link to its main page. Cover missing check-in/communication arrangements through those links rather than repeating the full instructions. Use a helpful tone. Sources: C Q3–6, L1 01:43–04:25 and 06:03, L2 01:18–03:03, L3 01:20–02:14.
- [ ] **Ready** — **B5: Communication that fits the trip.** On No cell service, explain that reception at the car is not a reliable plan for the route, plan a suitable emergency communication backup, and retain the reliable contact as another layer of preparation. Distinguish a downloaded map/GPS position from a device's ability to send an SOS. Verify device/network claims before adding them; neither a generic GPS device nor a satellite product is a promise of successful contact or immediate rescue. Do not require one product brand. Sources: C Q9, L2 05:06–05:54, L3 01:20–02:14, AdventureSmart trip-planning guidance. Emergency movement decisions stay in A2, not in a new reception-seeking checklist.

### C. Make the interviews visible through About

- [ ] **Liz** — **C1: The rider example on About.** Recommended placement: after Liz's motivation for the project, before links to practical help. A short draft is in `content.md`. Retain only the clear facts: an experienced rider fell while alone, could not reach his phone, and was heard by someone passing nearby who called 9-1-1. Connect the example to leaving a route and agreed check-in time with someone reliable. Keep the rider anonymous, omit medical/recovery details and precise identifying information, and label it as an account shared in an interview. Do not imply Liz attended the incident or that leaving a plan would have prevented the fall. Source: L1 01:43–04:25. Liz has suggested the placement; Ms. Lejeune's permission and review of the actual story wording are still needed. This is not a substitute for the separate water story requested in section 1.
- [ ] **Liz** — **C2: A small interview-learning section on About.** Alongside the story, show the contributors' verified roles, a short explanation of how the interviews informed the site, and three or four lessons linked to the relevant practical pages. Suitable themes: realistic planning, leaving a plan, preparing for a wait, and deciding when to turn around. Use a real approved quote sparingly; do not put a full transcript or repeated emergency instructions here. Retain the clear unofficial-site disclaimer. Place the sources here as already allowed in section 1; do not restore the removed Be aware source footer.
- [ ] **Liz** — **C3: One possible Home quote.** Christine's Q12 is a genuine candidate, not a new invented opening line. Liz chooses whether to use it, and Christine reviews the displayed text and attribution. Do not silently shorten or polish words inside quotation marks. A short Home link to About can make the project motivation discoverable without another set of advice cards.
- [ ] **Later** — **C4: A separate local-SAR page only if it adds enough.** For the first revision, About plus the existing practical pages is the recommended structure. A dedicated interview/lessons page could be useful if Liz later wants several approved stories, more interview material, or that page as a distinct portfolio feature. In that case, About should link to it rather than repeat it. Do not add a separate page just to hold the same tips again.

### D. Review and acceptance

- [ ] **Ready** — **D1: Keep a source for every new claim.** Draft public copy in `content.md` first. Use own-word summaries for general points and keep a file/question or audio timestamp in the source notes. Quotes and personal accounts remain identifiable as such. Christine's real 7 km / 900 m example in Q6 is distinct from her earlier hypothetical 6 km / 1,200 m example; neither is a universal difficulty limit or an identified route. No invented water story, replacement quotation, gear item, or billing claim.
- [ ] **Liz** — **D2: Arrange the review already offered.** Send the concrete relevant draft passages to Christine, and request Ms. Lejeune's permission and review for her attribution and rider story. These requests are not sent by this task. Resolve A2 with a qualified reviewer. Do not label the entire website “SAR approved” from one interview or a review of selected text. Existing detailed first-aid, avalanche, and water-response cards are not validated by these interviews and need their own qualified source review before being represented as checked.
- [ ] **Ready** — **D3: Check the integrated site when implementation is authorized.** Keep each full explanation on its main page and check all shorter summaries for consistency. Confirm source/permission status, compare `content.md` with the HTML, check links and emergency-number prominence, and preview the changed pages on phone and desktop. Immediate emergency actions must be visible without expanding a box. Keep the current shared disclaimer. Mark these tasks done only after the actual integration and checks, then publish only when Liz requests it.

**Suggested order:** A1 and the A2 review first; B1–B3 with A3 next; B4–B5 and summary links after that; About/quote integration as the permissions arrive. A general source-backed correction does not need to wait for permission to use a personal story. Nothing in this section marks the remaining website work complete.

## Next up

1. **Ready** — Use the prepared 9-1-1 draft for the emergency revision (A1). Liz arranges the related movement/group-separation review (A2). Implementation and the review are still open.
2. **Ready** — Draft/integrate the focused preparation improvements when authorized: planning, a shared packing baseline, turnaround decisions, and preparation for a wait (B1–B3 and A3).
3. **Liz** — Review the About story draft and obtain Ms. Lejeune's permission; choose any Home quote and obtain Christine's review (C1–C3). The About story placement is agreed; no extra advice page is needed for this revision.
4. **Liz** — Choose the project name and finish the remaining personal writing and school deliverables. General safety improvements need not wait for a water story.
5. **Ready** — Responsive, mobile-first design so the site adapts automatically on iPhone, iPad, and desktop. Independent design review and the Print/PDF feature remain later work.

## Open questions

- Where is the official rubric or requirement checklist?
- Where does the portfolio live (Obsidian, a school portal, or somewhere else), and should this repository link to it?
- Are the remaining course interviews already scheduled?
- Thank-you notes: handwritten or email? Are there drafts?
- Is Instagram still in scope?
- When can Christine review the concrete drafts, and can Ms. Lejeune approve the proposed use of her story and attribution?
- Who will review the detailed first-aid, avalanche, and water-response passages that the interviews do not validate?
