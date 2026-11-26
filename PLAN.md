# Plan

Outdoor Safety — Sea-to-Sky · [Live website](https://lzl462.github.io/outdoorsafety/)

Deadline: Monday 30 Nov 2026. Status reconciled on 26 Nov after pulling the thirteen-part presentation and Instagram starter kit and receiving confirmation that the account exists.

The website's content baseline, interviews, redesign, trip planner, reviewed refinements, expanded presentation draft and Instagram starter kit are complete as repository artifacts. Remaining work is mainly Liz's personal presentation/portfolio answers, rehearsal and social publication details. The detailed earlier implementation history is in [the historical plan](docs/history/PLAN-2026-11-25.md).

## Current scope

All eight items from the [follow-up review](reviews/2026-11-25-follow-up.md) are implemented. The latest slice completes R05's source-supported story clarification and R06's shorter contents labels, alongside the compact Quick reminders entry point. The completed visual direction is retained.

Liz subsequently approved Print & share and a small online trip planner. [Print & share](resources.html), linked from the shared footer and About, now gathers the online plan, existing blank sheet, A6 sign preview/PDF and website QR. [Trip Plan](trip-plan.html) processes entries in the browser, validates core details/times and creates reviewed text for copying/email drafts plus a compact print layout from the same formatted fields. There is no account, server submission, automatic delivery or return monitoring. Short and normal filled examples now fit one A4/Letter page; genuinely long notes continue without truncation. The blank sheet still prints on one A4/Letter page.

The [trail-sign concept](prototypes/trail-sign.html) remains a labelled design preview. Its unchanged QR opens [Quick reminders](tips.html), which now has four visible preparation prompts and a direct Trip Plan action, keeping its emergency guidance and seven detailed reminders. The earlier separate briefing is a reference prototype, not another maintained entry page. Real placement and multilingual work remain separate.

The navigation follow-up makes Trip Plan the first direct destination under Prepare in every shared menu and footer. The preparation guide is now labelled “Before your trip”; existing URLs and anchors are retained. The sticker uses only “Outdoor Safety · Sea-to-Sky” as its small project label; personal/school attribution remains in the website context rather than on the artwork. Its PDF and PNG preview have been regenerated.

The user confirmed that the email and QR functions have been tested and are adequate for this school project's scope. Those functional checks are complete. Physical printer tests are explicitly out of scope because no printer is available; they are not outstanding completion work. The recorded browser/PDF checks remain valid evidence.

The three-agent [decision review](reviews/2026-11-25-optional-refinements.md) is now implemented: two story sentence edits, three shorter guide contents labels and a compact preparation entry on existing Tips. Parallel implementation was followed by source/editorial and presentation-usability cross-reviews.

[Presentation](presentation.html) is a temporary rehearsal aid with thirteen English parts, optional Previous/Next practice mode and twenty-one deliberate demo links. Since 25 Nov its order follows the recorded Capstone requirements and teacher's five questions: Who I am, Why, My question, How I did it, What rescuers taught me, What I made, Trip Plan, QR sign and poster, Challenges, Core competencies, Next steps, Thank you and Possible questions. Highlighted `[Liz: …]` placeholders mark text only Liz can supply. A short cue sheet at the end follows the same thirteen parts with keywords and Show prompts, plus a copy button for phone notes and manual-selection fallback. Copied text comes directly from the visible list. The complete outline and cue sheet work without JavaScript. Its final subdued menu entry is marked `data-presentation-link`, so it can be removed from the menu later while the page stays available. This is a practice draft, not evidence that the panel presentation or physical poster is finished.

The school documents were supplied in the other Grok conversation. Their original files and full wording are absent from this checkout; this plan retains the imported requirements summary rather than claiming an independent check against the complete rubric. The [26 Nov review](reviews/2026-11-26-presentation-social-status.md) recommends keeping the full rehearsal bank while choosing a short core around who/why/product/learning/next steps, with selected demos and the Q&A held in reserve.

The user confirmed on 26 Nov that the Instagram account has been created. [The starter kit](social/instagram/README.md) tracks six single-image drafts, one three-slide carousel, captions and profile options. The actual handle and which posts are live are awaiting confirmation. Artwork, captions and website advice are maintained together in the repository; the publication record distinguishes exports from confirmed uploads.

From now on, feature, navigation and advice changes must include a review of the presentation's detailed speaking points, demo links and short cue sheet/Show prompts, keeping all three in sync and updating affected text in `content.md` and `presentation.html`. This is also recorded in [AGENTS.md](AGENTS.md).

## Open work and decisions

“Unverified” means completion is not evidenced in this repository; it does not mean Liz has not done it elsewhere.

| Owner / status | Remaining item | Evidence and boundary |
| --- | --- | --- |
| Liz / rehearsal | Practise a short core presentation and choose which demos fit the reported open-house table format. | [Thirteen-part outline](presentation.html) covers the imported rubric summary and teacher's five questions, with a short cue sheet. Choose a small number of demos; keep detailed timeline, statistics and Q&A available for follow-up. No fixed speaking time is recorded in the imported notes. |
| Liz / to fill | Replace the remaining `[Liz: …]` placeholders in the presentation (first in `content.md`, then `presentation.html`). | Still missing: inquiry question and strand, proposal-to-product link and what to show for it, which parts she did herself, how she kept going while waiting for interview answers and a before/after example, and what she would change. Optional: what the Sea-to-Sky outdoors means to her, a personal reason, an interview surprise, skills for her studies, anyone else to thank. Facts already used are recorded in `content.md` (About, 10 Oct sheet, 23 Oct check-in, 25 Nov details). |
| Liz / unverified | Write the final self-reflection for the teacher. | Ten questions and a rubric (depth, required components, structure/mechanics, evidence) are in the Capstone package p. 25–26. Not tracked in this repository. |
| Liz / unverified | Portfolio components: proposal with inquiry question, timeline, bi-weekly journal and MLA bibliography. | Listed in the imported package summary (p. 20–21). The 10 Oct competency sheet, 23 Oct check-in and later personal details are summarized in content.md; they do not establish that the full portfolio is finished. About's source list is not MLA-formatted. |
| Liz / to confirm | Record the Instagram handle and any posts already published. | Account creation is confirmed by the user on 26 Nov. The earlier username was a suggestion. Add confirmed dates/URLs to [the publication record](social/instagram/README.md); do not infer uploads from the nine PNG exports. A website account link or follow QR can use the confirmed handle if wanted. |
| Recommended / maintenance follow-up | Make the Instagram renderer use this repository's paths before the next regeneration. | src/build.py still assumes `/workspace/instagram-kit` and `google-chrome`; it does not regenerate overview.png. Existing eleven artwork HTML files match the generator, but the original path is not portable to this checkout. The README records the editing workflow and limitation. |
| Later / optional menu cleanup | Remove the temporary Presentation menu link when it is no longer useful for practice. | It is the final subdued entry, marked `data-presentation-link` in the shared menus. Removing it does not require changing visitor routes or deleting the rehearsal page. |
| Liz / decision | Keep the current project name or choose the final one. | Outdoor Safety — Sea-to-Sky is still described as a working title. If it changes, update site branding/page titles and print materials; the old global sidebar no longer exists. |
| Liz / unverified | Complete or confirm her own interview notes and portfolio interview page. | The source interviews and transcripts are ready. They do not prove that Liz's personal notes or interview page are finished. The portfolio's location is unknown; it is not in the tracked repository. |
| Liz / unverified | Check whether any further course interviews are required. | The Capstone package (received 25 Nov) does not set an interview count. Two contributors are documented. |
| Liz / unverified | Build or confirm the physical poster board using the existing layout. | [The cardboard layout](pdfs/trifold.html) is a safety poster. The teacher's email asks the board to show Liz's story, passion and accomplishments too, so side panels for who/why/process/competencies/next steps are suggested. A file does not prove that the board has been made. |
| Liz / unverified | Complete or confirm thank-you notes to Christine Strub and Laure Lejeune. | No sent-note or completed physical-note evidence is tracked here. This plan is not an instruction to send messages. |
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
| Done | Archival of duplicate print sheets/build script and a structural validation command. | archive/; [checker](scripts/check_site.py). Current run passes 20 public HTML files and 735 local references, including Presentation and the two concept pages. Explicit page/landmark/disclaimer contracts and stylesheets are checked; nine structural regression tests pass. The separate social artwork is inventoried in its README, outside the website checker's page set. |
| Done | Six bounded follow-up corrections after the independent review. | R01–R04 and R07–R08 in the [review record](reviews/2026-11-25-follow-up.md#implementation-follow-up). Targeted Chromium/WebKit focus/layout checks and Chromium accessibility, menu and poster/PDF checks passed. |
| Done / design preview | A6 trail-start QR sign and concise mobile-briefing prototype. | [Prototype notes](prototypes/README.md), editable HTML/CSS/SVG, PNG preview and one-page PDF. The code was decoded from the actual PNG/PDF and opens `tips.html`. Resources exposes the design; no physical installation is claimed. |
| Done | Print & share page and online trip planner. | [Acceptance record](reviews/2026-11-25-planning-acceptance.md). Five logic tests plus browser validation/export/fallback checks; Chromium/WebKit layouts and Unicode email handoff checked. The 26 Nov compact print correction fits short and normal filled examples on one A4 and Letter page, with all fields retained; long content flows without truncation. The user's practical email/QR acceptance is recorded below. |
| Done / user confirmed | Practical email and QR functional checks. | On 25 Nov, the user confirmed testing both functions and accepted them as adequate for the project's scope. No further email/QR acceptance test is outstanding. |
| Done | Three independent reviews and implementation of the remaining refinements. | [Decision review and implementation follow-up](reviews/2026-11-25-optional-refinements.md#implementation-follow-up): source-supported R05 wording, compact R06 labels and the Tips entry point, with independent cross-review. |
| Done / rehearsal aid | English project presentation with a lightweight practice mode and short cue sheet. | [Presentation](presentation.html): thirteen parts (rubric-based order since 25 Nov), twenty-one demo links, full-outline fallback, Previous/Next boundaries and return from demos. Short prompts with Show cues can be copied to phone notes. Chromium/WebKit layouts, selected accessibility rules, canonical copied-text parity, clipboard success/denial paths and no-JavaScript cue access pass. AGENTS.md explicitly requires detailed notes, demo links and cue sheet to stay in sync. |
| Done / answered | Competency examples filled from Liz's submitted sheet. | The 10 Oct “Connecting Your Competencies” sheet supplies the SD48 categories (Learn, Create & Innovate, Think Critically, Contribute, Collaborate) and personal examples. BC names appear in brackets where they fit. Any question about the final reflection's “six Core Competencies” wording belongs to that separate school reflection, not an empty presentation section. |
| Done / draft assets | Instagram starter kit tracked in the repository. | 021b916: nine 1080 × 1350 post images, two profile options, crop/overview previews, website QR, captions and eleven generated artwork HTML files. [Maintenance and publication record](social/instagram/README.md). Confirmed publication is separate. |
| Done / user confirmed | Instagram account created. | User report on 26 Nov; the actual handle has not yet been supplied. Current presentation notes and cue sheet reflect the created account. |
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
- Optional local-rescuer feedback, if Liz wants it. Instagram is now in scope with an account and repository-managed starter drafts, as recorded above.
- A richer presentation tour with cross-page overlays is a final optional idea only if time remains. The current outline and one-part rehearsal mode already support practice; no overlay system is implemented.
- Deferred multilingual website: French, German, Spanish and Italian alongside English. Start with the concise trail-start briefing; expand to the main guides later if useful. Retain one stable QR and English fallback, use language names, and check translations against the canonical safety meaning. This is lower priority than the sign/entry-page concept; no translations or language switcher are implemented now.

## Evidence and limits

- The [historical plan](docs/history/PLAN-2026-11-25.md) preserves the detailed content/source mapping, review findings, implementation steps and original acceptance evidence. The chronological [worklog](WORKLOG.md) is retained rather than rewritten.
- School-specific requirements below reflect the summary imported from Grok, not a new audit of the original package/email. The remaining personal answers and completed portfolio cannot be inferred from the website files. Roughly 80+ hours remains a labelled estimate from the later weekly-time description, not a counted work log.
- Recorded implementation checks cover Chromium/WebKit layouts and reader journeys, selected automated accessibility rules, no-JS/storage-failure behavior and actual Chromium PDF exports. The blank trip plan and short/normal filled examples each use one A4 and Canadian Letter page in those exports; long filled notes may span multiple pages.
- Today's [follow-up review](reviews/2026-11-25-follow-up.md) and [decision review](reviews/2026-11-25-optional-refinements.md) retain their original observations and the completed follow-up implementations. All eight initial refinements are closed. These reviews are not a clinical/field audit.
- The user's reported email/QR tests are accepted for this project's scope; the test device and method are not recorded. Additional native Apple-device checks are optional. Physical printer tests are explicitly excluded. The physical poster, real calls/SOS and external school/outreach completion are separate from browser evidence and functional email/QR acceptance.

## Working rules

Keep PLAN.md, WORKLOG.md and AGENTS.md in English. Start new public wording in content.md before editing HTML. Do not invent quotations, stories or equipment items, and do not state that rescue in B.C. is free. Use the existing repository/verified sources for pack lists. Keep Presentation's detailed notes, demo links and short cue sheet/Show prompts in sync with affected feature, navigation and advice changes; keep affected Instagram captions, artwork source and exports aligned too. Record confirmed social publication separately from prepared drafts. Publish only when asked; the user authorized the three refinements and in-app presentation, continuing the earlier commit/push instructions. Retain the labelled design previews and keep larger planner/multilingual/overlay features deferred.
