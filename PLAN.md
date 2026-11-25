# Plan

Outdoor Safety — Sea-to-Sky · [Live website](https://lzl462.github.io/outdoorsafety/)

Deadline: Monday 30 Nov 2026. Status reconciled on 25 Nov against repository revision ae4220f and Liz's feedback in this conversation.

The website's content baseline, interview integration, redesign and first wording follow-up are complete. Most remaining work is personal school/presentation work or a decision by Liz. The detailed implementation history has moved to [the historical plan](docs/history/PLAN-2026-11-25.md).

## Current scope

This pass is documentation and review only. Website files stay unchanged. Six agents reviewed the current state in two passes; their separate [small-improvement proposals](reviews/2026-11-25-follow-up.md) are for tomorrow's discussion, not an accepted implementation backlog. Liz can choose any, defer them or leave the current design as it is.

## Open work and decisions

“Unverified” means completion is not evidenced in this repository; it does not mean Liz has not done it elsewhere.

| Owner / status | Remaining item | Evidence and boundary |
| --- | --- | --- |
| Liz / tomorrow | Review the separate improvement proposals and decide what, if anything, to implement. | Initial positive design feedback and the requested interview-wording change have already been received and acted on. No further website changes are authorized by this review request. |
| Liz / decision | Keep the current project name or choose the final one. | Outdoor Safety — Sea-to-Sky is still described as a working title. If it changes, update site branding/page titles and print materials; the old global sidebar no longer exists. |
| Liz / unverified | Complete or confirm the portfolio and her own interview notes. | The source interviews and transcripts are ready. They do not prove that the three notes, Interview page or portfolio are finished. The portfolio's location is unknown; it is not in the tracked repository. |
| Liz / unverified | Check the actual school rubric and whether any further course interviews are required. | Two contributors are documented. The rubric is absent, so the old “remaining interviews” line is an unanswered course-requirement question, not proof that interviews still need doing. |
| Liz / unverified | Build or confirm the physical cardboard/poster using the existing layout. | [The cardboard layout](pdfs/trifold.html) is ready; a file does not prove that the board has been made. |
| Liz / unverified | Print the website QR for the poster/flyer and test scanning from the finished material. | [Print QR](images/qr-website-print.svg) and [the QR used by the layout](images/qr-website.svg) exist. Physical printing/scanning is not evidenced. |
| Liz / unverified | Complete or confirm thank-you notes to Christine Strub and Ms. Lejeune. | No sent-note or completed physical-note evidence is tracked here. This plan is not an instruction to send messages. |
| Liz / optional decision | Decide whether Instagram is still in scope. | Only a draft name/bio exists. If wanted, Liz creates the account and supplies the handle; posts and a follow QR then become possible. These are not missing website prerequisites. |
| Later / device access | Hands-on Safari/iPhone/iPad and physical-printer checks. | Chromium and automated WebKit checks are recorded; those are not native Apple-device or physical-printer tests. |

## Completed deliverables

| Status | Result | Evidence |
| --- | --- | --- |
| Done | Genuine attributed Home quotation and completed public project introduction. | [Home](index.html), [About](about.html); latest public introduction simplified at ae4220f. |
| Done | Useful hiking and biking examples with practical links and source distinctions. | [About: hiking](about.html#hiker-story), [About: rider](about.html#rider-story). Empty Emergency-page prompts are removed. |
| Done | Interview source collection, independent transcription and website integration. | [Interview sources](interviews/), three timestamped Codex transcripts; f5654fd and 37eaea8. Liz's own portfolio work remains separate. |
| Done | Preparation, shared essentials/activity notes, turnaround advice and clear emergency orientation. | [Before you leave](checklists.html), [Essentials & activities](pack-lists.html), [Be aware](be-aware.html), [What to do if](if.html). Content findings closed at 08bfc4d. |
| Done | No-cell-service page and consistent shared disclaimer. | [No cell service](no-service.html), content pages and print artifacts. |
| Done | One-page handwritten trip plan and browser Print / Save as PDF workflow. | [Trip plan](pdfs/before-you-leave.html), [dedicated stylesheet](pdfs/trip-plan-one-page.css); 15c8992. Guide/reminder printing included in the redesign. |
| Done | Full responsive redesign, grouped navigation, direct emergency access and locally saved packing checks. | Ten content pages plus 404; 2c79f56. |
| Done | Three licensed local website photographs, local fonts and source/credit information. | [Image notes](images/README.md), [About credits](about.html#photo-credits), fonts/ licences. This describes the redesigned website pages; the cardboard layout still uses external photo URLs. |
| Done | Cardboard layout and website QR source assets. | [Layout](pdfs/trifold.html), [print QR](images/qr-website-print.svg). Physical completion remains unverified above. |
| Done | Initial implementation reviews and targeted follow-up wording. | Three design reviewers, recorded browser/accessibility/PDF checks, then Liz's audio-detail simplification at ae4220f. |
| Done | Archival of duplicate print sheets/build script and a structural validation command. | archive/; [checker](scripts/check_site.py). Current run passes 15 public HTML files and 495 local references; coverage refinements are only proposals. |
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

## Optional later ideas

These are not required completion work and do not authorize implementation now:

- Additional genuine stories, quotations or a distinct interview page only if new material has a clear use.
- A download/offline bundle or extra digital trip-planning route only if useful; evaluate existing official tools before building a custom form/backend.
- Generated illustrations if they improve the final presentation. Current regional photographs already have documented licences.
- Pruning unused legacy image files. Photo replacement/local delivery is complete; removal of every unused asset was deliberately not done.
- Instagram and optional local-rescuer feedback, if Liz keeps those ideas in scope.

## Evidence and limits

- The [historical plan](docs/history/PLAN-2026-11-25.md) preserves the detailed content/source mapping, review findings, implementation steps and original acceptance evidence. The chronological [worklog](WORKLOG.md) is retained rather than rewritten.
- Recorded implementation checks cover Chromium/WebKit layouts and reader journeys, selected automated accessibility rules, no-JS/storage-failure behavior and actual Chromium PDF exports. The trip plan is one page on A4 and Canadian Letter in those exports.
- Today's [follow-up review](reviews/2026-11-25-follow-up.md) is a bounded read-only review with fresh perspectives and counter-review. Its findings are proposals, not completed fixes or a new clinical/field audit.
- Native Apple devices, physical printers, real calls/SOS, the physical poster/QR and external school/outreach completion are not certified by repository files or browser emulation.

## Working rules

Keep PLAN.md, WORKLOG.md and AGENTS.md in English. Start new public wording in content.md before editing HTML. Do not invent quotations, stories or equipment items, and do not state that rescue in B.C. is free. Use the existing repository/verified sources for pack lists. Publish only when Liz asks; the current request authorizes documentation commit/push, not website changes.
