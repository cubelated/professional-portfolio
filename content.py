"""Bilingual portfolio copy grounded in the supplied professional profiles."""
from pathlib import Path
import html

ROOT = Path(__file__).parent
ORIGIN = "https://cubelated.com"
E = html.escape

CONTENT = {'en': {'lang': 'en',
        'path': '/',
        'title': 'Hanssen Budisantoso Wijaya | Software Engineer in Taiwan',
        'description': 'Explore Hanssen Budisantoso Wijaya’s portfolio: full-stack platforms, Flutter mobile apps, '
                       'and systems integration. Software engineer in Taichung, Taiwan.',
        'skip': 'Skip to content',
        'code': 'Source code',
        'visit': 'Visit product',
        'caseLabels': ['The idea', 'What I built', 'Engineering focus'],
        'projects': [{'name': 'Renewables',
                      'type': 'Personal product',
                      'category': 'Mobile · Web',
                      'tagline': 'Life has deadlines. Your memory deserves a break.',
                      'description': 'An independently built life-admin app for passports, subscriptions, '
                                     'warranties, and other things with an expiry date.',
                      'tags': ['Flutter', 'Riverpod', 'Supabase', 'FCM', 'RevenueCat'],
                      'repo': 'renewables',
                      'url': 'https://renewables.cubelated.com/',
                      'case': ['Keep important dates in one place, with recurring reminders that fit '
                               'everyday routines.',
                               'Built the Flutter/Riverpod app with calendar views, home-screen widgets, '
                               'local and push notifications, and cloud synchronization.',
                               'Integrated Supabase, Firebase/FCM, and RevenueCat for backend data, '
                               'notifications, and subscription access.']},
                     {'name': 'Selah',
                      'type': 'Personal project',
                      'category': 'Mobile experience',
                      'tagline': 'A little less scrolling. A little more stillness.',
                      'description': 'A guided devotional app that helps people pause, open a physical '
                                     'Bible, reflect, and journal.',
                      'tags': ['Flutter', 'Riverpod', 'Drift / SQLite'],
                      'repo': 'selah',
                      'case': ['A devotional app should support time away from the screen, while giving '
                               'people enough structure to begin.',
                               'Built guided sessions with pause and restore, encrypted local journaling, '
                               'and password-protected export and restore.',
                               'Keeping personal reflections on the device while making interrupted sessions '
                               'resumable. Data stays local; encrypted exports provide a manual backup '
                               'path.']},
                     {'name': 'IFGF Planner',
                      'type': 'Community project',
                      'category': 'Web application',
                      'tagline': 'Fewer scheduling puzzles. More time for people.',
                      'description': 'A volunteer scheduling and absence-management platform for church '
                                     'teams, with automated scheduling, reminders, and coordinator tools.',
                      'tags': ['React', 'Vite', 'Supabase', 'Cloudflare', 'LINE Messaging API'],
                      'repo': 'ifgf-planner',
                      'case': ['Make recurring service schedules easier to coordinate around roles and '
                               'changing availability.',
                               'Developed volunteer scheduling, absence reporting, coordinator workflows, '
                               'and LINE reminders and notifications.',
                               'Check eligibility and availability while keeping organizational data scoped '
                               'and public form links time-limited.']}],
        'imageAlt': 'Renewables mobile dashboard showing urgent and upcoming expiry dates',
        'jobs': [('Jun 2024 — May 2026',
                  'Lead Software Engineer',
                  'HostingInside LTD',
                  ['Led six engineers and expanded a DCIM platform across three data centers. Optimized '
                   'POS data retrieval across tens to hundreds of thousands of records, reducing read '
                   'times from 1–2 minutes to approximately 3 seconds.']),
                 ('May 2022 — May 2024',
                  'Software Engineer',
                  'HostingInside LTD',
                  ['Built infrastructure monitoring for 70+ devices and resolved Linux, networking, and '
                   'infrastructure incidents across 100+ customer environments.']),
                 ('Sep 2022 — Jan 2024',
                  'Software Maintainer',
                  'Feng Chia University',
                  ['Maintained a learning platform serving 200+ students, with a Flutter frontend, Next.js '
                   'backend, and Docker deployment.']),
                 ('Jul 2022 — Dec 2022',
                  'Project Engineering Intern',
                  'Talent Circulation Alliance',
                  ['Collaborated in a six-person team on Flyfitnity, connecting a Flutter app with Raspberry '
                   'Pi motion sensors. The project received a TCA Honorable Award.'])],
        'expertise': [('Mobile development', '', 'Flutter · Dart · Kotlin · Riverpod'),
                      ('Full-stack development', '', 'React · Next.js · PostgreSQL · Supabase · Firebase'),
                      ('Systems & integration', '', 'Linux · Docker · Redis · WebSocket · REST APIs')],
        'aboutText': ['I’m Hanssen, an Indonesian software engineer based in Taichung, Taiwan. Over 4+ '
                      'years, I’ve built production applications, connected infrastructure systems, and led '
                      'a six-person engineering team. I enjoy taking software from the first sketch through '
                      'deployment—and making the complicated parts feel simple.'],
        'degrees': [('M.S. Information Engineering & Computer Science', 'Feng Chia University · 2024', ''),
                    ('B.S. Information Engineering & Computer Science', 'Feng Chia University · 2022', ''),
                    ('English · Mandarin · Indonesian',
                     'Professional English · Working Mandarin · Native Indonesian',
                     '')]},
 'zh': {'lang': 'zh-Hant',
        'path': '/zh-tw/',
        'title': '黃晟旺 Hanssen｜台中軟體工程師・全端與 Flutter 開發',
        'description': '黃晟旺（Hanssen Budisantoso Wijaya）的個人作品集。台中軟體工程師，專注全端開發、Flutter 行動應用與系統整合。探索 Renewables、Selah、IFGF Planner 等專案與工作經歷。',
        'skip': '跳至主要內容',
        'code': '查看原始碼',
        'visit': '前往產品網站',
        'caseLabels': ['專案構想', '開發內容', '技術重點'],
        'projects': [{'name': 'Renewables',
                      'type': '個人產品',
                      'category': '行動應用・網頁',
                      'tagline': '生活有期限，記憶力可以休息一下。',
                      'description': '獨立設計與開發的生活管理應用，集中追蹤護照、訂閱、保固及各種重要期限。',
                      'tags': ['Flutter', 'Riverpod', 'Supabase', 'FCM', 'RevenueCat'],
                      'repo': 'renewables',
                      'url': 'https://renewables.cubelated.com/',
                      'case': ['把重要日期放在同一處，搭配週期性提醒，減少日常記憶負擔。',
                               '以 Flutter／Riverpod 開發行動應用，提供行事曆、主畫面小工具、本機與推播通知，以及雲端同步。',
                               '整合 Supabase、Firebase／FCM 與 RevenueCat，串接後端資料、通知及訂閱權限管理。']},
                     {'name': 'Selah',
                      'type': '個人專案',
                      'category': '行動體驗',
                      'tagline': '少滑一點螢幕，多留一點安靜。',
                      'description': '引導使用者暫停忙碌、打開實體聖經，透過反思與日誌，建立有節奏的靈修流程。',
                      'tags': ['Flutter', 'Riverpod', 'Drift / SQLite'],
                      'repo': 'selah',
                      'case': ['靈修應用應幫助使用者離開螢幕，同時提供足夠的引導，讓人更容易開始。',
                               '建立可暫停與恢復的引導式靈修流程、加密本機日誌，以及以密碼保護的匯出與還原功能。',
                               '讓個人反思留在裝置上，也讓中斷的靈修能繼續進行。資料僅儲存於本機，透過加密匯出提供手動備份方式。']},
                     {'name': 'IFGF Planner',
                      'type': '社群專案',
                      'category': '網頁應用',
                      'tagline': '少一點排班難題，多一點相聚時間。',
                      'description': '為教會團隊開發的志工排班與缺席管理平台，整合自動排班、提醒通知及協調員管理功能。',
                      'tags': ['React', 'Vite', 'Supabase', 'Cloudflare', 'LINE Messaging API'],
                      'repo': 'ifgf-planner',
                      'case': ['依照角色與不斷變動的出席狀況，協助團隊安排固定服事。',
                               '開發志工排班、缺席回報與協調員管理流程，並整合 LINE 提醒與通知。',
                               '檢查志工資格與可參與時段，以組織範圍限制資料存取，並為公開表單連結設定有效期限。']}],
        'imageAlt': 'Renewables 行動應用主畫面，顯示緊急與即將到期的事項',
        'jobs': [('2024.06 — 2026.05',
                  '資深軟體工程師',
                  '鷹式特網有限公司 · HostingInside',
                  ['帶領六人工程團隊，將 DCIM 平台擴展至三座資料中心。優化 POS 系統數萬至數十萬筆資料的讀取流程，將耗時從 1–2 分鐘縮短至約 3 秒。']),
                 ('2022.05 — 2024.05',
                  '軟體工程師',
                  '鷹式特網有限公司 · HostingInside',
                  ['建置管理 70+ 台設備的基礎架構監控系統，並處理 100+ 客戶環境的 Linux、網路及基礎架構事件。']),
                 ('2022.09 — 2024.01',
                  '軟體維護工程師',
                  '逢甲大學',
                  ['維護支援 200+ 名學生的學習平台，涵蓋 Flutter 前端、Next.js 後端與 Docker 部署。']),
                 ('2022.07 — 2022.12',
                  '專案工程研習生',
                  '人才循環大聯盟 · TCA',
                  ['與六人跨領域團隊合作開發 Flyfitnity，串接 Flutter 應用與 Raspberry Pi 動作感測硬體，專案榮獲 TCA 佳作獎。'])],
        'expertise': [('行動應用開發', '', 'Flutter · Dart · Kotlin · Riverpod'),
                      ('全端開發', '', 'React · Next.js · PostgreSQL · Supabase · Firebase'),
                      ('系統整合與基礎架構', '', 'Linux · Docker · Redis · WebSocket · REST APIs')],
        'aboutText': ['我是黃晟旺（Hanssen），來自印尼，目前居住於台中。具 4 '
                      '年以上軟體工程經驗，曾開發正式上線的應用、整合基礎架構系統，並帶領六人工程團隊。我喜歡從構想到部署全程參與，把複雜留給程式，把簡單留給使用者。'],
        'degrees': [('資訊工程學系 碩士', '逢甲大學 · 2024', ''),
                    ('資訊工程學系 學士', '逢甲大學 · 2022', ''),
                    ('英文・中文・印尼文', '英文流利・中文工作溝通・印尼文母語', '')]}}
