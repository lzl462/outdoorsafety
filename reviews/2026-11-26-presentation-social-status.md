# Presentation and Instagram status review — 26 Nov 2026

Reviewed the pulled commits b9b910b (expanded presentation) and 021b916 (Instagram kit), current files and the user's confirmation that the Instagram account exists. This is a repository-based editorial/status review, not a new review by multiple agents.

## Initial assessment, before the speaking revision

The expansion was a useful improvement for a school presentation. It explained Liz's motivation, inquiry, process, learning and next steps alongside the product. The submitted competency examples, explicit AI assistance and distinction between interview evidence and news were good foundations. Personal placeholders and the length needed a follow-up; that implementation is recorded below.

The original speaking points contained roughly 1,600 words, before Show prompts and source notes. The recommendation was a short core around who / why / product / learning / next steps, with one or two deliberate demos. The detailed timeline, rescue-call figures, additional links and Q&A could stay available for follow-up. No new speaking-time requirement was assumed.

## Requirements recorded in the imported notes

The school package/email were supplied in the other Grok conversation; those original files remain absent from this checkout. The approved proposal was subsequently supplied and is now checked directly in [docs/school](../docs/school/README.md). This table maps the recorded requirements to current evidence; it does not certify the complete final rubric.

| Recorded requirement / question | Current presentation evidence | Remaining personal work |
| --- | --- | --- |
| Who is presenting? | Part 1: Liz, school and international background; mentor thanked in Part 12. | Practise in her own voice. |
| Why this project? | Part 2: purpose, audience, hiking case and local context. | Optional personal motivation; use the strongest short example. |
| Inquiry and proposal-to-product link | Part 3 expresses the awareness campaign's purpose from the supplied proposal. The comparison is recorded in docs/school/README.md. | Comparison complete for this proposal; multilingual and undocumented outreach plans are distinguished from delivered outputs. |
| Process and overcoming problems | Parts 4 and 9: Liz's confirmed interview/page/Instagram work and a concrete AI/GitHub/responsive-design example, with the dated timeline in optional notes. | Practise the example and the distinction between her work and AI support. |
| Product and visual aids | Parts 6–8: website, Trip Plan, QR concept and poster layout. | Choose demos and confirm the physical board; the safety-poster layout alone does not show the whole personal capstone story. |
| Core competencies | Part 10 uses the supplied SD48 sheet, with concrete examples. | Select examples she can explain naturally. The full school document has not been independently compared with the imported competency mapping. |
| Next steps | Part 11 connects research/communication/digital skills with further study, alongside future language/sign ideas and @outdoorsafety48. | Instagram publication record remains separate. |
| Answering questions | Part 13: evidence, official status, privacy, own work/AI, testing and a proposed next improvement. | Use this as reserve and adapt the words during practice. |
| Portfolio and final reflection | Listed separately in PLAN.md from the imported package summary. | Their completion cannot be inferred from the website or transcripts. The 80+ hour figure remains a labelled estimate, not a counted log. |

## Status corrections made

- PLAN.md now reflects the thirteen-part draft, the Instagram kit/account and the current 20-page / 735-reference website check. Removed duplicate “decide whether Instagram is in scope” and “account not created” tasks.
- Updated canonical source notes, detailed presentation, short cue sheet and caption metadata from “social account planned” to the user's confirmed created-account status. The user subsequently confirmed @outdoorsafety48 as the actual handle; exports do not establish which posts are live.
- Added an Instagram README mapping each of the seven post topics to website sources, with a publication-date/URL column and a simple maintenance workflow. AGENTS.md now includes keeping captions, artwork source and exports aligned with changed website advice.
- The worklog's “Not committed” statements describe draft moments. Both pulled changes are now committed as b9b910b and 021b916; the reconciliation entry closes that status without rewriting the earlier chronology.
- Earlier source notes that still described supplied personal facts as placeholders now point to the subsequent competency/personal-detail sections. The October check-in's recorded hours stay distinct from the later estimated total.

## Instagram maintenance assessment

Keeping this small kit in the repository is practical: captions, editable source and final exports can be reviewed together, and version history preserves the work. Six single-image drafts plus one three-slide carousel are a useful bounded starting set. Upload manually from the prepared files and record the actual post URL/date. An export, account creation and a published post are three different states.

All nine post PNGs are 1080 × 1350. Both profile options are 1080 × 1080. The overview and final carousel slide were visually inspected. All eleven generated artwork HTML files match the generator's current strings. The artwork advice follows the existing website; campaign headings and calls to action are adaptations, so the previous “all wording from content.md” description was too absolute.

At this review, `src/build.py` still hardcoded `/workspace/instagram-kit` and invoked `google-chrome`, and did not regenerate the overview/crop comparison. This was resolved in the later [Instagram launch revision](2026-11-26-instagram-launch.md): paths are repository-relative and the renderer refreshes both previews. The user will upload manually.

## Source spot-check and limits

The [RCMP June release](https://rcmp.ca/en/bc/squamish/news/2026/06/4354387) supports the imported account of four calls in seven hours and a fifth the next day, including callers who had communication devices. Keep the existing qualification that these numbers describe demand rather than prove lack of preparation. The [Pique article](https://www.piquenewsmagazine.com/local-news/pemberton-search-and-rescue-calls-climb-40-amid-wildfires-backcountry-emergencies-12631133) returned HTTP 403 during this pass; its earlier recorded check was not independently repeated. The main pitch can use the hiking example without reciting every figure.

The user's report establishes account creation and the handle [@outdoorsafety48](https://www.instagram.com/outdoorsafety48/). Publication history has not been supplied. Accepted email/QR testing remains closed, and physical printer tests remain excluded.

## Validation

Chromium and WebKit passed 320/390/1440-pixel layouts, thirteen-step Previous/Next navigation and boundaries, twenty-one demo links, copied cue-sheet parity with content.md, manual-selection fallback and no-JavaScript access. Selected Chromium accessibility rules passed at 320/1440. Nine structural tests and the website check (20 HTML files, 735 local references) passed. No Instagram message or post was sent during this work.

## Implemented speaking revision — later on 26 Nov

The user confirmed that Liz conducted the interviews, spent many hours on the individual pages and now manages Instagram. The revised main speech states those contributions directly. AI-assisted wording/code and GitHub remain part of the process description. The learning example follows challenge → action → example → lesson: learning new tools, iterating with AI/GitHub, shortening contents links for phone use and checking the result. The specific label change is recorded in repository history; the new guide demo opens the unchanged full heading.

The user also clarified that the question is the purpose behind the overall teacher-approved project and then supplied the original proposal. Part 3 expresses that campaign's purpose as a guiding question. The proposal-to-product comparison is complete and linked from the extra notes. All personal placeholders have been removed from the current speaking page.

| Text measured the same way in the HTML | Before | After speaking revision |
| --- | ---: | ---: |
| Speaking points, including Q&A reserve | 1,621 words | 807 words |
| Competency speaking points | 295 words | 103 words |
| Phone cue sheet | 330 words | 137 words |

All thirteen stations and twenty-one demo options remain. Detailed timeline, estimated hours, source qualifications and portfolio context are kept in optional notes. The main instruction recommends one or two demos, with questions as reserve. The original portfolio/source sections stay in content.md; speech paraphrases and the guiding-question formulation are not presented as verbatim quotations from an interview or proposal.

The revised page passed Chromium/WebKit checks at 320/390/1440 pixels, all thirteen practice steps, the new learning-demo popup/return, cue copying/manual fallback and no-JavaScript access. Selected Chromium accessibility checks passed at 320/1440. All speaking-point lists and cue rows match content.md; the learning example and cue sheet were visually inspected on the phone layout. The site check still passes 20 HTML files and 735 local references.

## Original proposal received during the revision

The user supplied the five-page proposal dated 17 September as the approved project. It is preserved byte-for-byte in [docs/school/capstone-proposal-2026-09-17.pdf](../docs/school/capstone-proposal-2026-09-17.pdf), with a [source-to-product comparison](../docs/school/README.md). The speech now uses its personal motivation (outdoor sports, health and safety) and describes the product as a campaign combining website, QR materials and social media.

The proposal contains project-planning questions rather than a separately labelled research question or strand, and specifies no interview count. Its central campaign outputs are present. Multilingual content remains deferred; local-business collaboration and doctor/outdoor-professional interviews are not documented. Printable/downloadable resources support saved offline use; the whole website has no offline mode. These distinctions are available in the extra notes and comparison, rather than introducing new work into this presentation revision.

The concurrent remote poster-sketch commit 5ec694e was merged with both worklog entries preserved. The plan now links the hand sketch and keeps the physical board marked as unverified. The proposal PDF link adds one local reference, bringing the current site check to 20 HTML files and 736 references.

The subsequent [Instagram launch revision](2026-11-26-instagram-launch.md) adds website/account QR access and updates the presentation's display-code notes. Its current speaking/cue counts are 821/137 words; the website check now covers 740 local references. The three ready post packages and physical display production steps are tracked in the updated plan.
