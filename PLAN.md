# Plan

Outdoor Safety — Sea-to-Sky · [Live website](https://lzl462.github.io/outdoorsafety/)

Deadline: Monday 30 Nov 2026. Status reconciled on 25 Nov against repository revision ae4220f, the follow-up reviews and Liz's subsequent implementation request.

The website's content baseline, interview integration, redesign and first wording follow-up are complete. Most remaining work is personal school/presentation work or a decision by Liz. The detailed implementation history has moved to [the historical plan](docs/history/PLAN-2026-11-25.md).

## Current scope

After the documentation-only review, Liz authorized the clearly beneficial small corrections and their commit/push. R01–R04 and R07–R08 from the [follow-up review](reviews/2026-11-25-follow-up.md) are now implemented and checked: visible keyboard focus, an explicit agreed calling time, clear bear-spray/RAPP wording, stronger structural checks and local poster photos. R05 (story chronology) and R06 (mobile contents labels) remain optional proposals; the completed redesign is retained.

Liz subsequently approved Print & share and a small online trip planner. [Print & share](resources.html), linked from the shared footer and About, now gathers the online plan, existing blank sheet, A6 sign preview/PDF and website QR. [Trip Plan](trip-plan.html) processes entries in the browser, validates core details/times and creates one reviewed text for copying, email drafts and printing. There is no account, server submission, automatic delivery or return monitoring. The blank sheet still prints on one A4/Letter page.

The [trail-sign concept](prototypes/trail-sign.html) is now available as a labelled design preview. Its real QR opens the existing Quick reminders page. The separate briefing remains a preview of a possible shorter version of that entry point; the actual Quick reminders page is retained. Real placement and multilingual work remain separate from this slice.

The navigation follow-up makes Trip Plan the first direct destination under Prepare in every shared menu and footer. The preparation guide is now labelled “Before your trip”; existing URLs and anchors are retained. The sticker uses only “Outdoor Safety · Sea-to-Sky” as its small project label; personal/school attribution remains in the website context rather than on the artwork. Its PDF and PNG preview have been regenerated.

The user confirmed that the email and QR functions have been tested and are adequate for this school project's scope. Those functional checks are complete. Physical printer tests are explicitly out of scope because no printer is available; they are not outstanding completion work. The recorded browser/PDF checks remain valid evidence.

Three agents have now independently reviewed the remaining optional story/label/trail-entry ideas. The [decision review](reviews/2026-11-25-optional-refinements.md) recommends two small story edits, a compact preparation lead-in on existing Quick reminders, and shorter guide labels as lower-priority polish. These are recommendations only; this review changed no website copy, code or QR assets.

## Open work and decisions

“Unverified” means completion is not evidenced in this repository; it does not mean Liz has not done it elsewhere.

| Owner / status | Remaining item | Evidence and boundary |
| --- | --- | --- |
| Reviewed / optional implementation | Apply the small R05 story clarification and, in the same small content update, R06 label polish if wanted. | [Decision review](reviews/2026-11-25-optional-refinements.md): two source-supported sentence edits; three shorter contents labels save about 104–115 pixels in measured phone layouts while preserving full headings/anchors. Labels are the lowest priority; neither item is required school-completion work. |
| Reviewed / optional next slice | Add a compact preparation lead-in to existing Quick reminders if adopting the trail-entry idea. | [Decision review](reviews/2026-11-25-optional-refinements.md): four brief prompts and direct Trip Plan access at the stable `tips.html` URL, preserving the menu/help and detailed reminders. Do not copy the prototype wholesale or add a parallel maintained page. Functional QR acceptance remains closed. |
| Liz / decision | Keep the current project name or choose the final one. | Outdoor Safety — Sea-to-Sky is still described as a working title. If it changes, update site branding/page titles and print materials; the old global sidebar no longer exists. |
| Liz / unverified | Complete or confirm the portfolio and her own interview notes. | The source interviews and transcripts are ready. They do not prove that the three notes, Interview page or portfolio are finished. The portfolio's location is unknown; it is not in the tracked repository. |
| Liz / unverified | Check the actual school rubric and whether any further course interviews are required. | Two contributors are documented. The rubric is absent, so the old “remaining interviews” line is an unanswered course-requirement question, not proof that interviews still need doing. |
| Liz / unverified | Build or confirm the physical cardboard/poster using the existing layout. | [The cardboard layout](pdfs/trifold.html) is ready; a file does not prove that the board has been made. |
| Liz / unverified | Complete or confirm thank-you notes to Christine Strub and Ms. Lejeune. | No sent-note or completed physical-note evidence is tracked here. This plan is not an instruction to send messages. |
| Liz / optional decision | Decide whether Instagram is still in scope. | Only a draft name/bio exists. If wanted, Liz creates the account and supplies the handle; posts and a follow QR then become possible. These are not missing website prerequisites. |
| Later / optional device access | Additional hands-on Safari/iPhone/iPad checks, if useful. | Chromium and automated WebKit checks are recorded. These additional device checks are not required to reopen the accepted email/QR work. Physical printer tests are excluded. |

## Completed deliverables

| Status | Result | Evidence |
| --- | --- | --- |
| Done | Genuine attributed Home quotation and completed public project introduction. | [Home](index.html), [About](about.html); latest public introduction simplified at ae4220f. |
| Done | Useful hiking and biking examples with practical links and source distinctions. | [About: hiking](about.html#hiker-story), [About: rider](about.html#rider-story). Empty Emergency-page prompts are removed. |
| Done | Interview source collection, independent transcription and website integration. | [Interview sources](interviews/), three timestamped Codex transcripts; f5654fd and 37eaea8. Liz's own portfolio work remains separate. |
| Done | Preparation, shared essentials/activity notes, turnaround advice and clear emergency orientation. | [Before your trip](checklists.html), [Essentials & activities](pack-lists.html), [Be aware](be-aware.html), [What to do if](if.html). Content findings closed at 08bfc4d. |
| Done | No-cell-service page and consistent shared disclaimer. | [No cell service](no-service.html), content pages and print artifacts. |
| Done | One-page handwritten trip plan and browser Print / Save as PDF workflow. | [Trip plan](pdfs/before-you-leave.html), [dedicated stylesheet](pdfs/trip-plan-one-page.css); 15c8992. Guide/reminder printing included in the redesign. |
| Done | Full responsive redesign, grouped navigation, direct emergency access and locally saved packing checks. | Ten content pages plus 404; 2c79f56. |
| Done | Three licensed local website photographs, local fonts and source/credit information. | [Image notes](images/README.md), [About credits](about.html#photo-credits), fonts/ licences. The cardboard layout now reuses the local Harmony Lakes and Howe Sound photos with its existing credits. |
| Done | Cardboard layout and website QR source assets. | [Layout](pdfs/trifold.html), [print QR](images/qr-website-print.svg). Physical completion remains unverified above. |
| Done | Initial implementation reviews and targeted follow-up wording. | Three design reviewers, recorded browser/accessibility/PDF checks, then Liz's audio-detail simplification at ae4220f. |
| Done | Archival of duplicate print sheets/build script and a structural validation command. | archive/; [checker](scripts/check_site.py). Current run passes 19 public HTML files and 646 local references, including the two concept pages. Explicit page/landmark/disclaimer contracts and root/print/concept stylesheet assets are checked; nine structural regression tests pass. |
| Done | Six bounded follow-up corrections after the independent review. | R01–R04 and R07–R08 in the [review record](reviews/2026-11-25-follow-up.md#implementation-follow-up). Targeted Chromium/WebKit focus/layout checks and Chromium accessibility, menu and poster/PDF checks passed. |
| Done / design preview | A6 trail-start QR sign and concise mobile-briefing prototype. | [Prototype notes](prototypes/README.md), editable HTML/CSS/SVG, PNG preview and one-page PDF. The code was decoded from the actual PNG/PDF and opens `tips.html`. Resources exposes the design; no physical installation is claimed. |
| Done | Print & share page and online trip planner. | [Acceptance record](reviews/2026-11-25-planning-acceptance.md). Five logic tests plus browser validation/export/fallback checks; Chromium/WebKit layouts and Unicode email handoff checked. Short filled-plan A4 output is one page; longer content flows to further pages without truncation. The user's practical email/QR acceptance is recorded below. |
| Done / user confirmed | Practical email and QR functional checks. | On 25 Nov, the user confirmed testing both functions and accepted them as adequate for the project's scope. No further email/QR acceptance test is outstanding. |
| Done / recommendations recorded | Three independent reviews of the remaining optional refinements. | [Decision review](reviews/2026-11-25-optional-refinements.md): source/editorial, measured mobile-navigation and trail-entry perspectives, with differences in priority reconciled. No proposed refinement was implemented in this review. |
| Done | Direct Trip Plan navigation, unambiguous preparation label and neutral sticker attribution. | Thirteen shared menus/footers now link directly to the form; guide labels say “Before your trip”. Thirty Chromium menu checks covered phone/desktop/short-height layouts, direct form navigation and no-JS fallback. Regenerated A6 PDF is one page; its QR and the PNG decode to the unchanged Quick reminders URL. |
| Done | GitHub Pages publication from main, repository root. | [README](README.md). Existing Git/SSH/credential configuration remains unchanged. |

## Superseded or deliberately dropped tasks

| Earlier item | Current decision |
| --- | --- |
| Different hike, ride and climb trip-plan variants | Replaced by one shared handwritten plan plus activity considerations. Do not recreate duplicate forms as unfinished work. |
| Two anonymous stories beside Emergency numbers | Replaced by the sourced hiking case and anonymous rider account on About. A water story is optional, not a missing completion requirement. |
| Put the website QR on Home | Explicitly dropped on 24 Nov. The QR is for physical materials; people already on the site do not need it. |
| Credit or replace the unidentified highway photograph | Resolved by removing it from the redesigned emergency page. |
| More pictures, a genuine quote and real stories | The initial goal is fulfilled by the current regional imagery, attributed quote and two activity examples. Further additions are optional. |
| A separate interview/SAR page | About already houses the project, interviews, stories and sources. No distinct additional page has been agreed. |
| General printing postponed | Basic printing/save-as-PDF is implemented. A dedicated download/offline bundle would be a separate optional expansion. |
| Further redesign/navigation work described as future | Completed at 2c79f56. Old descriptions in the historical plan refer to earlier snapshots. |
| Mandatory external SAR/speaker approval | Removed at Liz's request. Optional feedback is welcome if she wants it; no organization endorsement is claimed. |
| Physical printer tests | Explicitly excluded by the user on 25 Nov because no printer is available. Keep the completed browser/PDF evidence; do not reopen physical print testing as a completion requirement. |

## Optional later ideas

These are not required completion work and do not authorize implementation now:

- Additional genuine stories, quotations or a distinct interview page only if new material has a clear use.
- A download/offline bundle or further planning features only if useful. The bounded online form is now implemented; accounts, server storage, automatic reminders and return monitoring remain outside scope. Link to official tools before considering a larger planner.
- Generated illustrations if they improve the final presentation. Current regional photographs already have documented licences.
- Pruning unused legacy image files. Photo replacement/local delivery is complete; removal of every unused asset was deliberately not done.
- Instagram and optional local-rescuer feedback, if Liz keeps those ideas in scope.
- Deferred multilingual website: French, German, Spanish and Italian alongside English. Start with the concise trail-start briefing; expand to the main guides later if useful. Retain one stable QR and English fallback, use language names, and check translations against the canonical safety meaning. This is lower priority than the sign/entry-page concept; no translations or language switcher are implemented now.

## Evidence and limits

- The [historical plan](docs/history/PLAN-2026-11-25.md) preserves the detailed content/source mapping, review findings, implementation steps and original acceptance evidence. The chronological [worklog](WORKLOG.md) is retained rather than rewritten.
- Recorded implementation checks cover Chromium/WebKit layouts and reader journeys, selected automated accessibility rules, no-JS/storage-failure behavior and actual Chromium PDF exports. The trip plan is one page on A4 and Canadian Letter in those exports.
- Today's [follow-up review](reviews/2026-11-25-follow-up.md) records the original bounded read-only review and the subsequent six authorized corrections with targeted acceptance evidence. R05 and R06 remain proposals. Neither pass is a new clinical/field audit.
- The user's reported email/QR tests are accepted for this project's scope; the test device and method are not recorded. Additional native Apple-device checks are optional. Physical printer tests are explicitly excluded. The physical poster, real calls/SOS and external school/outreach completion are separate from browser evidence and functional email/QR acceptance.

## Working rules

Keep PLAN.md, WORKLOG.md and AGENTS.md in English. Start new public wording in content.md before editing HTML. Do not invent quotations, stories or equipment items, and do not state that rescue in B.C. is free. Use the existing repository/verified sources for pack lists. Publish only when Liz asks. She approved the Print & share/online-plan slice and the subsequent navigation/sticker follow-up, continuing the earlier commit/push instructions. Retain the labelled design previews and keep larger planner/multilingual features deferred.
