# Portfolio research and content decisions

## September 22 motion and project expansion

- Unified motion: hover 160 ms; expand/collapse and content opacity 240 ms; entry fades 320 ms; explicit header scrolling 480 ms. Reduced-motion changes settle running animations. Wheel, touch, keyboard and resize interrupt animated scrolling.
- The document title, social title and Site display name are Hanssen Budisantoso Wijaya.
- Added IFGF Cloud, Flyfitnity, LearnAlgo and VirtualClass as compact disclosures. Source: the user's `黃晟旺 (3).pdf`, dated 18 September 2026, pages 3–4. The saved `Profile (2).pdf` supplies supporting career context. The live LinkedIn fetch failed, so no claim is made to have read its current project section. No repository or live-product links were invented for these projects.
- Seven project entries in both languages. Mobile header wrapping, reduced-motion preferences, semantic native disclosures and interruption controls retained.

## September 22 visual revision

User-directed references: https://www.marco.fyi/ and https://perryw-2023.webflow.io/ . Reviewed their live layouts and visible navigation. The revision uses a compact Home / Work / Contact navigation, a dark typographic introduction, prominent project covers, and progressive disclosure to reduce visible text. Original English and Traditional Chinese content remains available. The supplied LOGO(1).png is used unchanged as the favicon and header mark.

Interaction details: scroll-aware navigation indicator, native scrolling, on-demand project and background details with height transitions, subtle entry and hover motion, and email copying with a visible result. Reduced motion disables animated transitions; essential content, navigation and disclosures remain functional without JavaScript. This static checkout does not have a supported managed browser-preview server; validation covers generated markup, local links/assets, JavaScript syntax, and exact logo identity, rather than claiming browser-level animation QA.

Reviewed 17 September 2026. This is a small purposive sample, not a statistical survey. Counts apply only to the five inspected homepages below; linked pages were not exhaustively audited. Observed headings are recorded literally. A biography can be unheaded; professional history can be in prose.

| Portfolio | Observed identity headline / introductory label | Observed topics and headings |
| --- | --- | --- |
| [Brittany Chiang](https://brittanychiang.com/) | Frontend Engineer | About; Experience; Projects; Writing; View Full Résumé |
| [Lee Robinson](https://leerob.com/) | Bio | Short biography with professional history; Notes; Blogs; contact email |
| [Tania Rascia](https://www.taniarascia.com/) | Hey, I'm Tania! | About me; A brief timeline; Latest; Shelves; Series; Projects; Resume |
| [Cassidy Williams](https://cassidoo.co/) | Software Engineer in Chicago | Introductory biography; blog; newsletter; github; socials; recent posts |
| [Shawn Wang](https://swyx.io/) | Learn in Public | About / My story; ideas; selected work and current initiatives; Latest writing & appearances; Selected talks; correspondence |

Across these five homepages, identity/background and writing links appear in all five. Current or previous professional work is described in all five, but not always in a dedicated Experience section. A Projects section or current-initiative showcase appears on three (Brittany, Tania, Shawn). All expose some way to follow, connect, or subscribe; these are not equivalent to a direct hiring contact. Explicit résumé links appear on two (Brittany and Tania). This sample is biased toward engineers who publish educational content; it does not justify treating a blog as mandatory for a hiring portfolio.

## Recommended information order

1. Identity and clear role: Software Engineer, location, and scope of work.
2. Selected work: three relevant projects, concise problem statements, technologies, product/source links, and optional engineering detail.
3. Experience: official titles, dates, concrete scope; do not inflate titles or insert unverified impact metrics.
4. Expertise: grouped capabilities linked to actual project experience; avoid percentage-based skill meters.
5. About: a brief human introduction, education, and language context.
6. Contact: direct email plus LinkedIn and GitHub.

Writing is common in this sample but omitted because no publishable article inventory was supplied. Likewise, no invented testimonials, client logos, download résumé button, or product adoption metrics.

## Headline choices

- English: Thoughtful products. Solid engineering.
- Traditional Chinese: 用心打造產品，以扎實技術實現。
- Selected work: Built around real needs. / 從真實需求出發。
- Experience: Building beyond the interface. / 不只介面，更深入系統。
- Expertise: The full product picture. / 從產品到系統，完整思考。
- About: Curious by nature. Practical by design. / 保持好奇，務實解題。
- Contact: Have a problem worth solving? / 有值得解決的問題嗎？

## UI and UX decisions

- English is the default at `/`; Traditional Chinese lives at `/zh-tw/`.
- Visible language names rather than flag icons. Each page is fully rendered HTML, with language and alternate URL metadata. Language links preserve the current section.
- Short navigation, real links, and native keyboard-operable expandable engineering notes.
- Clear type hierarchy, quiet blue emphasis, restrained motion, strong contrast, keyboard focus, skip link, responsive layouts, reduced-motion and print styles.
- Important content is readable without JavaScript. No contact form needing a nonexistent backend.
- Genuine Renewables interface image sourced from the user's product website: https://renewables.cubelated.com/app-phone.webp . It is an interface illustration, not evidence of an iOS release.
- Career copy uses known user-supplied history. Project notes describe scope and focus, not independently measured outcomes. Current availability and unverified adoption/performance claims are omitted.

## Implementation

Static HTML/CSS/JavaScript. `build.py` contains paired content dictionaries and generates both language pages. Hosting is isolated from the existing pixel-art portfolio. All source and final static output are tracked together.

## September 22 profile-based copy update

Read both newly attached PDFs locally: `Profile(1).pdf` (3 pages) and `104_黃晟旺.pdf` (6 pages). Updated English and Traditional Chinese bio, experience, capabilities, language proficiency, project summaries, and recruiting copy. Kept the three-link navigation and progressive disclosure. Added a brief factual highlight to each role and the TCA internship.

English Lead Software Engineer follows the LinkedIn PDF; Chinese 資深軟體工程師 follows the 104 resume. Both versions state six-person team leadership separately. Graduation years agree; conflicting bachelor graduation months are omitted. Removed the undated TOEIC score from the portfolio because the supplied certification dates are historical. No residential address, phone number, or other private resume fields were published.

The 80% improvement claim is omitted pending clarification of the measured workflow and baseline. VirtualClass uses award-neutral wording because the resume body says Excellence Award/優等獎 while the attachment caption says 佳作. Selah retains the existing previously sourced project facts. Added the exact Flyfitnity repository and LearnAlgo demo-playlist links embedded in the supplied 104 PDF. The organization's private-cloud login is not a public product demo and remains unlinked.

Requested follow-up media: current Selah and IFGF Planner screenshots or short recordings. Copy checks cover both rendered languages and preserve the supplied logo, motion settings, and responsive CSS.

## September 22 confirmed outcomes and supplied media

- The user confirmed VirtualClass received 佳作. Both languages now name this award explicitly; English uses Honorable Mention (佳作).
- The user clarified the POS improvement: reading tens to hundreds of thousands of records took 1–2 minutes before optimization and approximately 3 seconds afterward. Both versions now report those approximate read times directly, without implying an 80% reduction in total customer wait time or a universal benchmark.
- Inspected all supplied media locally: Selah logo, home screen, 90-second session recording, and IFGF Planner dashboard and monthly-schedule screenshots. Supplied images are optimized for web delivery without altering their contents. Original portfolio header/favicon logo is retained.
- The Selah card shows its own app logo and actual home screen. Its expandable section includes a silent, user-controlled walkthrough with a poster, no autoplay, no initial video preload, and a text description of the session sequence. Audio is omitted from this web demonstration. Closing the disclosure or leaving the tab pauses playback.
- The Planner cover uses the actual dashboard; its expandable section includes both full screenshots with accessible labels and full-size links. Images have explicit dimensions, lazy loading, and responsive sizing. Media remains accessible through native HTML without JavaScript.

## September 22 logo and interaction refinement

- Added the supplied Renewables logo (`cover_2(1).png`) to that product's card. The personal header/favicon logo is unchanged. Product logo styling is isolated from the angled phone screenshot.
- Expand/collapse now combines a 280 ms height transition with opacity and an 8 px slide, including reversal from the currently displayed state during repeated clicks. Closing content becomes inert, video pauses, and resize settles to natural height.
- Pointer hover gives all seven project summaries a 1.012 scale, 3 px lift and 6% brightness increase over 240 ms. Keyboard focus retains an explicit outline and brightness feedback. Reduced motion disables transforms.
- First-entry viewport reveals now cover hero text, background disclosure, headings, projects, contact elements and footer: 18 px upward motion over 380 ms, staggered at most 135 ms. Each plays once. Content is never CSS-hidden, remains usable without JavaScript, and active reveals cancel for keyboard focus or reduced-motion changes.

## September 23 motion preference diagnosis

The reported instantaneous hover changes match the former reduced-motion branch: CSS disabled all transitions and JavaScript skipped animations. This explains the symptom when the browser reports reduced motion; the user's actual browser preference has not been observed.

Added a bilingual footer Animations control (device setting, On, Reduced). A small script resolves the preference before CSS loads, and both CSS and JavaScript use that resolved value. Explicit On overrides the device setting only after the visitor chooses it; the default still honors the device. Choices persist locally across reloads/language changes. Reveals can initialize after switching from reduced to full motion. Storage failures fall back safely, and timing values have validated defaults.

Verification: JavaScript syntax, generated page/asset checks, and Node VM checks of both device states, explicit overrides, live device changes, saved preferences, invalid values, blocked storage, and effective durations all passed. This plain static Site has no supported managed browser preview, so browser visual behavior was not independently verified.

## September 23 requested motion removal, icons, language and research media

The user explicitly requested removing reduced-motion behavior. Removed the preference script, footer selector, all CSS reduction rules and all JavaScript device/preference gates. Normal durations always apply; unsupported Web Animations browsers retain native functional disclosures.

Added labeled inline icons to social links (GitHub, LinkedIn, YouTube), product links, email/copy actions, location, background and project headings. YouTube profile URL comes from the supplied 104 PDF. Replaced the language link with a labeled native dropdown, retaining section navigation and a no-script alternate link. Header uses two rows on narrower viewports to avoid crowding.

Inspected and integrated the supplied LearnAlgo and VirtualClass logos, both LearnAlgo comparison images and the VirtualClass poster. Added the provided YouTube playlist and video as explicit click-to-load embeds with direct-link fallbacks. Collapsing the project removes the iframe to stop playback. YouTube retrieval was unavailable during authoring; no claim is made to have independently watched the external videos or verified embedding permission. Supplied image contents are unchanged, with web encoding only.

## Spacing and motion review — 2026-09-23

- Aligned the sticky header edges with the page container at each breakpoint.
- Replaced fixed tablet headline sizes with fluid typography and switched featured cards to one column below 801 px.
- Moved Renewables and Selah cover text/media into separate grid columns to avoid overlap; reserved space for their bottom action indicator.
- Animated disclosure content instead of the complete details element so expanding content cannot clip a hovered summary. Preserved reversal, focus handling, native fallback, and media cleanup.
- Added consistent transitions to language selection and image outlines; reduced contact-link crowding on narrow screens.
- Derived native hash-scroll padding from the actual header height, including font-load and resize updates.
- Added a repository README describing editing, build, hosting, assets, and manual QA.
- Verified generated bilingual HTML, local media references, and JavaScript syntax. A mocked DOM check covers disclosure opening, rapid reversal, closing, and cleanup; CSS received a source review. A compatible browser preview is unavailable for this static Site; visual animation and device testing remain unverified.
