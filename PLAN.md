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

- [ ] **Liz** — About page: one new page about the website itself. Liz decides the content. Main focus (Liz, Nov 24): why a site like this matters and what made Liz start it: a school capstone project from the Sea-to-Sky area, because in 2026 there were many incidents where people went into the wilderness unprepared and were very lucky. Specific incidents only from real sources, none invented. Other possible parts: the sources the site is based on (the Be aware source line can return here), the interview with Christine Strub (only after she has reviewed it), and the note that this is not an official rescue site. Draft wording goes in `content.md` first.

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
- [ ] **Later** — Ask someone from search and rescue to look at the live pages.

## 5. Presentation / physical

- [ ] **Liz** — Build the cardboard from `pdfs/trifold.html`. The big title can change when the project name is chosen.
- [ ] **Liz** — Print the website QR for the trifold poster and any flyer. Print file: `images/qr-website-print.svg` (scalable, points to https://lzl462.github.io/outdoorsafety/). Make a new one if the site address changes. The QR is not needed on the website itself.

## 6. Website revision based on the interviews

Compared on 24 Nov 2026 with the current site pages and `content.md`. This section is planning only. New wording still goes in `content.md` first. Nothing from the interviews goes on the live site until Liz asks, and until the person quoted has reviewed it.

Sources:

- Christine Strub, Prevention Team Coordinator, Squamish Search and Rescue, member since April 2011. Written answers in `interviews/christine-strub-squamish-sar.md` (email, 27 Oct 2026). She said it is okay to quote her answers with her name and role, and she would like to review the text before it goes live.
- Ms. Lejeune, three voice messages on 5 Nov 2026: `interviews/Nov 5 at 10-01 AM.md`, `interviews/Nov 5 at 10-10 AM.md`, and `interviews/Nov 5 at 10-18 AM.md`. She introduces herself in the first recording as Miss Lejeune. The second and third recordings do not repeat her name; they continue the same answers and refer to Christine, so they belong to the same interview. She says she is a regular member of Squamish Search and Rescue, specialized in rope rescue and winter rescue, and that she coordinates training, budget, and gear for the winter team. The transcripts do not record permission to quote her on the website. Ask her before any of her words or stories go on the site, and let her review the wording.

Independent Codex working transcripts were added on 25 Nov 2026: `interviews/Nov 5 at 10-01 AM_codex.md`, `interviews/Nov 5 at 10-10 AM_codex.md`, and `interviews/Nov 5 at 10-18 AM_codex.md`. They recover much of the speech missing from the earlier versions, including the complete group-dynamics advice. One short phrase in the gut-feeling passage remains unresolved. Most source references below still point to the earlier transcripts; recheck wording and timestamps against the Codex versions and original audio before drafting public text. The website revision items remain open, and speaker review and permission are still required as described above.

Do not invent quotes, stories, or gear. Do not write that rescue in B.C. is free. Do not treat inaudible or unfinished lines in the transcripts as facts.

### Fix an error

- [ ] **Liz** — What to do if (`if.html`, and the matching lines in `content.md`). The hurt section now says: “Call 9-1-1 right away. Ask for police. They activate Search and Rescue.” Ms. Lejeune said there is no direct search-and-rescue line. You call 9-1-1, and 9-1-1 directs the call to fire, ambulance, or police, who then request the SAR team. If someone is lost, the call goes to the police, then to SAR. If someone is injured, the call goes to ambulance, then ambulance asks SAR for help. Source: `interviews/Nov 5 at 10-10 AM.md` (~03:06): “There is no direct search and rescue. What happens is you call 911 and they will direct you to Fire, Ambulance or Police…” The lost section’s “Ask for police” matches her lost-person path. The hurt section should not tell people to ask for police. The line on Be aware (`be-aware.html`) and No cell service (`no-service.html`), “This corridor does not have its own rescue line,” is consistent and can be expanded with this pathway. Draft the correction in `content.md` first. Needs Ms. Lejeune’s review before it goes live.

### Add a page

- [ ] **Liz** — Decide whether interview advice belongs on a new page (for example an Advice from local SAR page), in the About page already listed in section 1, or as short attributed lines on the existing pages. Do not put Christine’s or Ms. Lejeune’s words on the live site until they have reviewed them.

### Change a page

- [ ] **Liz** — Common mistakes (`mistakes.html`): the page has only three short lines. Expand it from the interviews, in our own words, in `content.md` first: using a social media photo as a plan, the false belief that “this cannot happen to me,” underestimating elevation gain, not leaving a trip plan, not packing for how cold it gets when you stop, and running out of daylight. If a line is attributed, it needs review by Christine or Ms. Lejeune first.

- [ ] **Liz** — Before you leave (`checklists.html` and, only if Liz wants the form changed, `pdfs/before-you-leave.html`): add a short planning list from Christine’s “before you head out” points that the trip plan does not already ask for: weather forecast, exposure such as avalanche terrain, communication coverage, water, what the elevation gain means, and how you get back. Source: `interviews/christine-strub-squamish-sar.md`, question 5. Changing the fill-in form is Liz’s decision. Needs Christine’s review if her wording is used.

- [ ] **Liz** — Pack lists (`pack-lists.html`): the hiking list already has most of the 10 essentials. The biking and climbing lists do not include a first aid kit, a lighter or fire starter, or an emergency blanket. Ms. Lejeune named snack, water, a warm layer, and a headlamp as the minimum; she then said a first aid kit is even better, and mentioned a lighter and emergency blankets as additions that could help. Christine pointed to the AdventureSmart essentials and added personal medication (for example an EpiPen or insulin) and a spare pair of glasses or contacts. Sources: `interviews/Nov 5 at 10-01 AM_codex.md` (~05:22); `interviews/christine-strub-squamish-sar.md`, question 10; https://www.adventuresmart.ca/the-three-ts/#takingtheessentials. Add only from these sources. Do not invent other items. Liz decides which lines go on the biking and climbing lists. Attribution needs review.

- [ ] **Liz** — Emergency stories (`emergency.html`): one candidate story is in Ms. Lejeune’s first recording: an experienced mountain biker riding alone fell, could not reach his phone, and was found only because someone passed nearby. The current plan in section 1 asks for one hike story and one water story. This is a biking story, and the interviews do not include a water story. Do not invent a water story. Use this only if Liz wants it, Ms. Lejeune agrees, and she has reviewed the wording. No name. Do not fill in inaudible parts. Source: `interviews/Nov 5 at 10-01 AM.md` (~01:04–04:01).

### Add text

- [ ] **Liz** — Home quote (`index.html`): a candidate from Christine, also waited on in section 1: “Don't go beyond your means (be honest) and make/leave a solid trip plan.” Source: `interviews/christine-strub-squamish-sar.md`, question 12. Liz decides. Needs Christine’s review before it goes live.

- [ ] **Ready** — Before you leave (`checklists.html`) and/or Tips (`tips.html`): explain AdventureSmart’s 3 T’s (Trip plan, Training, The Essentials) and link to the pages Christine named: https://www.adventuresmart.ca/programs/survive-outside/ and https://www.adventuresmart.ca/the-three-ts/#takingtheessentials. Source: `interviews/christine-strub-squamish-sar.md`, questions 5 and 10. Draft in `content.md` first. Needs Christine’s review if the site attributes the 3 T’s to her.

- [ ] **Ready** — Be aware (`be-aware.html`, “The trip has to match the people”) and Common mistakes (`mistakes.html`): add that trail distance is not the same as distance on flat ground, and that elevation gain is easy to underestimate. Christine described a group that planned for 7 km, did not account for 900 m of elevation gain, and needed a Squamish SAR response. Source: `interviews/christine-strub-squamish-sar.md`, question 6. The general point can be written in our own words. The specific example, if used, needs Christine’s review. Do not add names.

- [ ] **Ready** — Common mistakes (`mistakes.html`) and/or Be aware (`be-aware.html`): add that a social media photo is not a plan. People often want the place in the picture without knowing what the route takes, and should not stop at comments that call a hike easy. Check reliable sources such as a BC Parks page, a visitor centre, or a local climbing store, and talk to people who have done the trip. Sources: `interviews/christine-strub-squamish-sar.md`, questions 3 and 6; `interviews/Nov 5 at 10-18 AM.md` (~01:11): “Don't follow the social media or just the beautiful pictures of the beautiful hikes.” Draft in our own words. Attribution needs review.

- [ ] **Ready** — Common mistakes (`mistakes.html`): add the false belief Christine named, “this can not happen to me.” She said it can happen to anyone, and that preparedness cannot prevent every incident but can reduce how bad it is. Source: `interviews/christine-strub-squamish-sar.md`, question 3. Needs her review if quoted or attributed.

- [ ] **Ready** — Be aware (`be-aware.html`) and Tips (`tips.html`, the turn-around tip): add that going down is often harder than going up, and that turning around can be hard when people think they are almost there. Both interviews say this. Sources: `interviews/christine-strub-squamish-sar.md`, question 6: “also for most people it is easier to go up then to go down”; `interviews/Nov 5 at 10-10 AM.md` (~02:01), the way down is also hard, and people should turn around before they are exhausted. Draft in our own words. Attribution needs review.

- [ ] **Ready** — Be aware (`be-aware.html`, “Dark arrives on its own clock”) and Tips (`tips.html`): add that the forest gets darker sooner than open ground, and that people should watch both the time and how much trail is left. Source: `interviews/Nov 5 at 10-10 AM.md` (~01:18). Needs Ms. Lejeune’s review if attributed.

- [ ] **Ready** — Be aware (`be-aware.html`) or Tips (`tips.html`): add that a trip should match the season and the person’s skill at that activity. Start easy, especially at the start of a season or in a new sport. Being a strong hiker does not mean the same person is ready for a hard bike ride. Sources: `interviews/Nov 5 at 10-10 AM.md` (~00:03) and `interviews/Nov 5 at 10-18 AM.md` (~00:00). Needs Ms. Lejeune’s review if attributed.

- [ ] **Ready** — Tips (`tips.html`, “Call 9-1-1 early”) and What to do if (`if.html`): make it clear that it is okay to call 9-1-1 before the situation gets worse, and that if there is reception the operator or a SAR manager may be able to help over the phone. If someone is hurt and cannot continue, stay warm, do not try to move, keep the group together, and wait for instructions. Sources: `interviews/christine-strub-squamish-sar.md`, question 6: “before getting into more trouble, it is okay to call SAR to assist you,” and questions 7–8; `interviews/Nov 5 at 10-10 AM.md` (~03:06–05:06). Do not tell people to call SAR directly. Needs review by both if their wording is used.

- [ ] **Ready** — Tips (`tips.html`), What to do if (`if.html`), and No cell service (`no-service.html`): explain why help can take a long time. Volunteer teams have to gather, take the right gear, travel to the trailhead, and then hike, bike, or wait for a helicopter, and a helicopter is not guaranteed in bad weather or if none is available. While waiting, put on every layer, use an emergency blanket, and think about shelter or a fire if it is cold or wet. Sources: `interviews/Nov 5 at 10-01 AM.md` (~06:03); `interviews/Nov 5 at 10-10 AM.md` (~06:00); `interviews/christine-strub-squamish-sar.md`, questions 2 and 9. Do not add any sentence about billing, or that rescue is free. Needs review if attributed.

- [ ] **Ready** — Be aware (`be-aware.html`), Tips (`tips.html`, “Be prepared”), and Pack lists (`pack-lists.html`): add that people often underestimate how cold they get once they stop moving, especially if they are already sweaty. Bring an extra warm layer or a change of clothes, not only what feels warm while walking. Source: `interviews/Nov 5 at 10-01 AM.md` (~06:03). Needs Ms. Lejeune’s review if attributed.

- [ ] **Ready** — Before you leave (`checklists.html`), Tips (`tips.html`, the trip-plan tip), and Common mistakes (`mistakes.html`): strengthen the trip-plan advice for people who go alone. Ms. Lejeune said it is okay to go out alone, but at least one friend, partner, or roommate should know the plan. Christine said that if you have no other way to call for help, a reliable person with the trip plan can call 9-1-1 when you do not return. Sources: `interviews/Nov 5 at 10-01 AM.md` (~03:01) and `interviews/Nov 5 at 10-18 AM.md` (~01:11); `interviews/christine-strub-squamish-sar.md`, question 9. Attribution needs review.

- [ ] **Ready** — No cell service (`no-service.html`) and Be aware (`be-aware.html`, “Your phone is a weak plan”): say more clearly that in this area it is common to have signal at the parking area and none once you start, so a satellite messenger or emergency beacon should be part of the plan, not an afterthought. Sources: `interviews/Nov 5 at 10-10 AM.md` (~05:06), she mentions an inReach or SOS device; `interviews/christine-strub-squamish-sar.md`, question 9: “emergency beacon, satellite phone.” Prefer the generic wording unless Liz wants the product name. Needs review if attributed.

- [ ] **Later** — Be aware or Tips: Ms. Lejeune named a gut feeling as a reason to turn around. The Codex transcript also recovers her complete group-dynamics advice: turn around if people start to disagree or there is a weird dynamic, before pushing each other and making it worse. Use only if Liz wants it, with Ms. Lejeune's review if attributed. Source: `interviews/Nov 5 at 10-10 AM_codex.md` (~02:23–03:03). A short phrase near the end of the gut-feeling example remains `[unclear]`; do not complete or quote that phrase.

### Not used from the interviews

- Ms. Lejeune’s own backcountry leg injury and rescue by Whistler Search and Rescue is her personal story. It stays off the site unless she offers it and Liz wants it. Source: `interviews/Nov 5 at 10-01 AM.md` (~01:04).
- Christine did not share one stand-out rescue. She said every response is different. Do not invent one. Source: `interviews/christine-strub-squamish-sar.md`, question 2.
- Christine asked what kind of photos would help. That can be answered when Liz writes to her (see section 4). It is not a site-text change.

## Next up

1. **Liz** — Write the Home quote, the two emergency stories, and/or choose the project name. These unblock most of the public-facing work.
2. **Liz** — Fix the “ask for police” line on What to do if when someone is hurt, and decide how interview advice should appear on the site (section 6).
3. **Ready** — Responsive, mobile-first design so the site adapts automatically on iPhone, iPad, and desktop.
4. **Later** — Independent design review once the site structure is finished.
5. **Later** — Print/PDF feature (download key pages as PDF), after the remaining Liz writing is in.

## Open questions

- Where is the official rubric or requirement checklist?
- Where does the portfolio live (Obsidian, a school portal, or somewhere else), and should this repository link to it?
- Are the remaining course interviews already scheduled?
- Thank-you notes: handwritten or email? Are there drafts?
- Is Instagram still in scope?
- Who should do the search-and-rescue review?
