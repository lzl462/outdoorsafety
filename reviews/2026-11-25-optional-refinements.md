# Three optional refinements — decision review, 25 Nov 2026

Baseline: `95a8e5c`. Three independent agents reviewed the hiker story, mobile guide contents and the compact trail briefing. The coordinator checked the current source, re-opened the two CityNews reports and reconciled the recommendations. Agents changed no repository files; mobile comparisons used isolated browser contexts and temporary DOM text only. This record contains recommendations, not implemented website changes or new required school deliverables.

## Recommended priorities

| Priority | Topic | Decision | Smallest useful scope |
| --- | --- | --- | --- |
| 1 | Hiker-story wording (R05) | Make the small editorial correction. | Clarify the battery description and date the emergency call; preserve the rest of the account and its lessons. |
| 2 | Trail-entry briefing | Integrate a short preparation lead-in into existing Quick reminders. | Four brief prompts and a direct Trip Plan action, retaining shared navigation, emergency access and detailed reminders at `tips.html`. |
| 3 | Mobile contents labels (R06) | Include as low-priority polish in the next small content update. | Shorten three labels; retain the full headings, anchors and targets. It does not warrant a separate redesign task. |

## 1. Hiker story: two source-supported edits

The current About opening puts “His phone battery failed” before a successful emergency call without an explanation. This is a reading ambiguity, not an established factual falsehood. [CityNews's 7 September interview](https://vancouver.citynews.ca/2026/09/07/squamish-bc-missing-hiker-found-shares-story/) reports that he realized during the hike that the battery would not last the return. [The 4 September report](https://vancouver.citynews.ca/2026/09/04/squamish-hiker-found-alive/) explicitly dates the emergency call to 1 September.

Suggested replacements for the existing opening paragraph, for a later canonical-copy update:

- “His phone battery failed.” → “During the hike, he realized his phone battery would not last the way back.”
- “He called 9-1-1 during that time” → “He called 9-1-1 on 1 September”.

Keep the trip-plan/wife point, source links and separate stay-put guidance. Add no phone-recovery explanation, extra medical details or incident reconstruction. The source reviewer recommends the edit with high confidence; both other reviewers independently noticed the reading ambiguity but deferred incident facts to the source check.

## 2. Trail entry: a compact addition on the existing page

The sign already opens `tips.html`. Quick reminders currently starts with generic disclosure instructions, navigation and a large emergency block. Its seven detailed preparation/local reminders are initially collapsed. The prototype makes four preparation answers visible, but has no direct online-Trip-Plan link and lacks the shared menu introduced since it was drafted. Adopting it unchanged would lose recent navigation improvements.

The entry reviewer measured these current/prototype differences in Chromium:

| Viewport | First preparation heading on current Tips | First question on prototype |
| --- | ---: | ---: |
| 320 × 568 | y932 | y423 |
| 390 × 844 | y829 | y418 |

These are observations of two different layouts/headers, not a prediction for an integrated version. Existing essentials/leave-a-plan links are already visible on the first screen. The prototype is not uniformly shorter: at 320 pixels its main section was about 1727 pixels tall versus 1682 for current Tips. The opportunity is preparation emphasis and order, not simply page height.

Recommended integration:

1. Keep Quick reminders and its stable `tips.html` URL, shared header/menu and visible Help/9-1-1 access.
2. Reuse the generic introduction/navigation space for an always-visible “Before you start” block with four short prompts: route/group fit; conditions/turnaround; trusted contact/plan/calling deadline; essentials/delay/no signal.
3. Include a direct “Make a trip plan” action to `trip-plan.html`.
4. Keep the useful emergency guidance and seven detailed reminders available. Do not prepend the prototype's four full paragraphs or maintain a second full entry page repeating the advice.

The entry reviewer recommends this small integration now, with moderate confidence in its UX benefit and high confidence in the observations. The other reviewers support the same integration boundaries if the idea is adopted. No separate URL, QR regeneration, backend or full layout swap is justified.

## 3. Mobile labels: worthwhile small polish

Recommended labels on Before your trip:

| Current contents label | Suggested label |
| --- | --- |
| The three T’s | The three T’s |
| Check the conditions for your actual route | Route conditions |
| Four checks before you go | Four planning checks |
| Give your contact a job, not just a destination | Your contact’s role |

The mobile reviewer compared current live text with these temporary DOM-only replacements after fonts loaded:

| Viewport | Current contents height | Suggested labels | First guide content, current → proposed |
| --- | ---: | ---: | ---: |
| 320 × 568 | 303 px | 188 px | y882 → y767 |
| 390 × 844 | 292 px | 188 px | y759 → y655 |

The online and printable plan actions already fit in the initial viewport at both sizes. The improvement is scanning/reaching the guide sooner, not repairing a blocked main journey. Link targets remained at least 44 pixels and condition/contact jumps still reached their complete headings below the sticky header.

“Four checks” saves another row at 390 pixels, but “Four planning checks” retains the topic and count. Prefer that clarity over the final 52 pixels. Keep all full section headings and anchor IDs.

The mobile reviewer recommends this as a small, low-priority change; the source reviewer calls it conditional polish; the entry reviewer would defer it as a standalone task. The coordinator recommends including the three label edits in a small content batch, while keeping them below the story and entry-point work in priority.

## Boundaries

These are expert reviews and browser comparisons, not a visitor study or proof of increased engagement. Existing reader journeys work. A later implementation needs only source/canonical-copy consistency and the affected mobile journeys checked. Email/QR functional acceptance stays closed; physical printer tests remain excluded. No additional permission process, framework, major redesign or new safety procedure is proposed.
