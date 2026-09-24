"""Static, bilingual portfolio. Native disclosures keep every detail accessible."""
from content import CONTENT, ROOT, ORIGIN, E
import json
from icons import icon
from additional_projects import EXTRA_PROJECTS

UI = {
 'en': {'nav':['Home','Work','Contact'],'hello':'Hi, I’m Hanssen.','hero':'Software with<br><span>purpose.</span>','intro':'I build mobile apps, web platforms, and connected systems that make everyday work feel simpler.','location':'Software Engineer · Taichung, Taiwan','scroll':'Explore selected work','background':'A little about me','work':'Selected work','selected':'03 projects','open':'Explore project','close':'Close details','contact':'Good things start<br>with a <span>conversation.</span>','say':'Hiring for full-stack, mobile, or systems engineering?','email':'Email me','copy':'Copy email','copied':'Email copied','failed':'Couldn’t copy. Use the email link.','links':'Elsewhere','footer':'Built with purpose.','back':'Back to top','renew':'Keep what matters.<br>Never miss a date.','selah':'Pause.<br>Breathe.<br><i>Begin.</i>','planner':'People.<br>Plans.<br><span>Connected.</span>','renewSubtitle':'Life admin, simplified.','selahSubtitle':'A little space for stillness.','plannerSubtitle':'A clearer way to coordinate.','more':'Experience & skills'},
 'zh': {'nav':['首頁','作品','聯絡'],'hello':'你好，我是黃晟旺 Hanssen。','hero':'用軟體，<br><span>解決真實問題。</span>','intro':'打造行動應用、網頁平台與整合系統，讓日常工作少一點繁瑣。','location':'軟體工程師 · 台灣台中','scroll':'探索精選作品','background':'多認識我一點','work':'精選作品','selected':'03 個專案','open':'探索專案','close':'收起內容','contact':'好的合作，<br>從<span>對話</span>開始。','say':'正在尋找全端、行動應用或系統整合工程師嗎？','email':'寄信給我','copy':'複製信箱','copied':'已複製信箱','failed':'無法複製，請使用信箱連結。','links':'也可以在這裡找到我','footer':'用心打造。','back':'回到頂端','renew':'重要的事，<br>不再錯過期限。','selah':'停下。<br>呼吸。<br><i>開始。</i>','planner':'團隊。<br>安排。<br><span>連結。</span>','renewSubtitle':'把生活瑣事，變得簡單。','selahSubtitle':'為安靜，留一點空間。','plannerSubtitle':'更清楚的團隊協調方式。','more':'經歷與技能'}
}

def ext(url,label):
    symbol = 'github' if 'github.com' in url else 'linkedin' if 'linkedin.com' in url else 'youtube' if 'youtu' in url else 'globe'
    return f'<a href="{E(url)}" target="_blank" rel="noopener noreferrer">{icon(symbol)}<span>{E(label)}</span>{icon("external")}</a>'

def extra_media(p,c):
    isen = c['lang']=='en'
    media = ''
    if p.get('videoEmbed'):
        label = 'Watch playlist' if p['slug']=='learnalgo' and isen else '觀看播放清單' if p['slug']=='learnalgo' else 'Watch project video' if isen else '觀看專案影片'
        media += f'<div class="video-embed"><a class="video-launch" href="{E(p["url"])}" target="_blank" rel="noopener noreferrer" data-embed="{E(p["videoEmbed"])}" data-video-title="{E(p["name"])} — {label}">{icon("youtube")}<span>{label}<small>YouTube · {E(p["name"])}</small></span>{icon("play")}</a></div>'
    for file,w,h,caption in p.get('media',[]):
        full = 'View full-size image' if isen else '查看完整尺寸圖片'
        media += f'<figure class="project-media"><a href="/media/{file}.webp" target="_blank" rel="noopener noreferrer" aria-label="{full}: {E(caption)}"><img src="/media/{file}.webp" alt="{E(caption)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a><figcaption>{E(caption)} {icon("external")}</figcaption></figure>'
    return media

MEDIA = {
 'en': {'home':'Selah home screen with a forest scene and Start Session button',
        'dashboard':'IFGF Planner dashboard showing upcoming services and scheduling status',
        'schedule':'IFGF Planner monthly schedule with volunteer roles and open assignments',
        'dashboardCaption':'Dashboard overview', 'scheduleCaption':'Monthly volunteer schedule',
        'full':'View full-size screenshot', 'video':'Selah session walkthrough',
        'videoCaption':'A quiet-time session, from beginning to end · 1:30 · Silent walkthrough',
        'flow':'Breathe → Check in → Gratitude → Scripture → Reflect → Pray → Carry it forward.',
        'fallback':'Download the session walkthrough'},
 'zh': {'home':'Selah 首頁，顯示森林場景與開始靈修按鈕',
        'dashboard':'IFGF Planner 儀表板，顯示近期聚會與排班狀態',
        'schedule':'IFGF Planner 每月排班表，顯示志工角色與待安排欄位',
        'dashboardCaption':'團隊儀表板', 'scheduleCaption':'每月志工排班',
        'full':'查看完整尺寸截圖', 'video':'Selah 靈修流程示範',
        'videoCaption':'從開始到結束，體驗一次靈修流程・1 分 30 秒・無聲示範',
        'flow':'深呼吸 → 心情確認 → 感恩 → 讀經 → 反思 → 禱告 → 帶入生活。',
        'fallback':'下載靈修流程示範影片'}
}

def project_media(index,m):
    if index == 1:
        return f'''<figure class="project-media session-demo"><video controls playsinline preload="none" width="720" height="1544" poster="/media/selah-poster.webp" aria-label="{m['video']}" aria-describedby="selah-video-caption selah-video-description"><source src="/media/selah-walkthrough.mp4" type="video/mp4"><a href="/media/selah-walkthrough.mp4">{m['fallback']}</a></video><figcaption id="selah-video-caption">{m['videoCaption']}</figcaption><p id="selah-video-description" class="video-description">{m['flow']}</p></figure>'''
    if index == 2:
        images = [('planner-dashboard', 'dashboard', 'dashboardCaption', 1898, 870), ('planner-schedule', 'schedule', 'scheduleCaption', 1900, 869)]
        return '<div class="project-gallery">' + ''.join(f'''<figure class="project-media"><a href="/media/{file}.webp" target="_blank" rel="noopener noreferrer" aria-label="{m['full']}: {m[caption]}"><img src="/media/{file}.webp" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{m[alt]}"></a><figcaption>{m[caption]}</figcaption></figure>''' for file,alt,caption,w,h in images) + '</div>'
    return ''

def project(p,c,u,index):
    slug=p.get('slug',p.get('repo')); compact=index>=3; typ=['renew','selah','planner'][index] if not compact else ''
    m=MEDIA['en' if c['lang']=='en' else 'zh']
    visual = '' if compact else f'<span class="cover-words">{u[typ]}</span>'
    if index == 0:
        visual += f'<img class="renew-screen" src="/renewables.webp" alt="{E(c["imageAlt"])}" width="1080" height="1920" loading="lazy">'
    elif index == 1:
        visual += f'<img class="selah-screen" src="/media/selah-home.webp" alt="{m["home"]}" width="600" height="1286" loading="lazy" decoding="async">'
    elif index == 2:
        visual += f'<img class="planner-screen" src="/media/planner-dashboard.webp" alt="{m["dashboard"]}" width="1898" height="870" loading="lazy" decoding="async">'
    case=''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a,b in zip(c['caseLabels'],p['case']))
    links=(ext(p['url'],p.get('linkLabel',c['visit'])) if p.get('url') else '')+(ext('https://github.com/cubelated/'+p['repo'],c['code']) if p.get('repo') else '')
    logo_file = {0: 'renewables-logo', 1: 'selah-logo'}.get(index) or p.get('logo')
    logo = f'<img class="project-logo" src="/media/{logo_file}.webp" width="32" height="32" alt="" loading="lazy">' if logo_file else ''
    cover = '' if compact else f'<span class="cover {typ}"><span class="cover-top"><span class="cover-brand">{logo}{E(p["name"])}</span><span>0{index+1}</span></span>{visual}<span class="cover-bottom">{E(u[typ+"Subtitle"])}</span><span class="explore" aria-hidden="true">↗</span></span>'
    return f'''<article class="project reveal {"compact-project" if compact else ""}"><details class="project-details" id="project-{slug}"><summary aria-label="{E(u['open'])}: {E(p['name'])}">
      {cover}
      <span class="project-heading"><span><span class="project-name">{(logo or icon(p.get('icon','briefcase'))) if compact else ''}{E(p['name'])}</span><span class="project-category">{E(p['category'])}</span></span><span class="expand-icon" aria-hidden="true">+</span></span>
      <span class="summary-caption">{E(p['tagline'])}</span>
    </summary><div class="details-content"><div class="project-copy"><p>{E(p['description'])}</p><ul class="tags">{''.join(f'<li>{E(t)}</li>' for t in p['tags'])}</ul>{project_media(index,m)}{extra_media(p,c)}<dl>{case}</dl><div class="project-links">{links}</div></div></div></details></article>'''

def render(key,c):
    u=UI[key]; isen=key=='en'
    project_count = f'{len(c["projects"])+len(EXTRA_PROJECTS[key]):02d}' + (' projects' if isen else ' 個專案')
    navigation=''.join(f'<a href="#{anchor}" {"aria-current=location" if anchor=="home" else ""}>{label}</a>' for anchor,label in zip(['home','work','contact'],u['nav']))
    langlink='/zh-tw/' if isen else '/'
    language='繁中' if isen else 'EN'
    langlabel='Switch to Traditional Chinese' if isen else '切換至英文'
    jobs=''.join(f'<li><span class="job-date">{E(date)}</span><strong>{E(role)}</strong><span>{E(company)}</span><p class="job-summary">{E(items[0])}</p></li>' for date,role,company,items in c['jobs'])
    skills=''.join(f'<div><h3>{E(a)}</h3><p>{E(t)}</p></div>' for a,b,t in c['expertise'])
    schools=''.join(f'<p><strong>{E(a)}</strong><br>{E(b)} {E(t)}</p>' for a,b,t in c['degrees'])
    person_id = ORIGIN + '/#person'
    website_id = ORIGIN + '/#website'
    page_url = ORIGIN + c['path']
    schema = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Person', '@id': person_id,
         'name': 'Hanssen Budisantoso Wijaya', 'alternateName': ['黃晟旺', 'Hanssen Budi'],
         'jobTitle': 'Software Engineer', 'url': ORIGIN + '/',
         'homeLocation': {'@type': 'Place', 'name': 'Taichung, Taiwan'},
         'knowsAbout': ['Full-stack development', 'Flutter', 'Mobile application development', 'Systems integration'],
         'sameAs': ['https://github.com/cubelated',
                    'https://www.linkedin.com/in/hanssen-budisantoso-wijaya/',
                    'https://www.youtube.com/@cubelated']},
        {'@type': 'WebSite', '@id': website_id, 'url': ORIGIN + '/',
         'name': 'Cubelated', 'alternateName': 'Hanssen Budisantoso Wijaya',
         'inLanguage': ['en', 'zh-Hant'], 'publisher': {'@id': person_id}},
        {'@type': 'ProfilePage', '@id': page_url + '#webpage', 'url': page_url,
         'name': c['title'], 'description': c['description'], 'inLanguage': c['lang'],
         'isPartOf': {'@id': website_id}, 'mainEntity': {'@id': person_id}}
    ]}
    return f'''<!DOCTYPE html>
<html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#111111"><title>{E(c['title'])}</title><meta name="description" content="{E(c['description'])}">
<link rel="canonical" href="{ORIGIN+c['path']}"><link rel="alternate" hreflang="en" href="{ORIGIN}/"><link rel="alternate" hreflang="zh-Hant" href="{ORIGIN}/zh-tw/"><link rel="alternate" hreflang="x-default" href="{ORIGIN}/"><meta property="og:type" content="website"><meta property="og:title" content="{E(c['title'])}"><meta property="og:description" content="{E(c['description'])}"><meta property="og:url" content="{ORIGIN+c['path']}"><meta property="og:locale" content="{'en_US' if isen else 'zh_TW'}">
<meta property="og:site_name" content="Cubelated"><meta property="og:locale:alternate" content="{'zh_TW' if isen else 'en_US'}"><meta property="og:image" content="{ORIGIN}/logo.png"><meta property="og:image:alt" content="Cubelated logo"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{E(c['title'])}"><meta name="twitter:description" content="{E(c['description'])}"><meta name="twitter:image" content="{ORIGIN}/logo.png"><meta name="twitter:image:alt" content="Cubelated logo">
<link rel="icon" href="/logo.png?v=2" type="image/png"><link rel="apple-touch-icon" href="/logo.png?v=2"><link rel="stylesheet" href="/styles.css?v=9"><script src="/app.js?v=9" defer></script><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body><a class="skip" href="#main">{c['skip']}</a><header class="header"><a href="#home" class="brand" aria-label="Hanssen Budisantoso Wijaya — {u['nav'][0]}"><img src="/logo.png" alt="" width="36" height="42"><span>Hanssen Budisantoso Wijaya</span></a><nav class="nav" aria-label="{'Main navigation' if isen else '主要導覽'}"><span class="nav-track" aria-hidden="true"></span>{navigation}</nav><label class="language-picker" for="site-language">{icon('globe')}<span class="sr-only">{'Language' if isen else '語言'}</span><select id="site-language" data-language aria-label="{'Language' if isen else '語言'}"><option value="/" lang="en" {'selected' if isen else ''}>English</option><option value="/zh-tw/" lang="zh-Hant" {'' if isen else 'selected'}>繁體中文</option></select>{icon('chevron')}</label><noscript><a href="{langlink}">{language}</a></noscript></header>
<main id="main"><section id="home" class="hero shell" aria-labelledby="hero-title"><p class="hello">{u['hello']}</p><h1 id="hero-title">{u['hero']}</h1><div class="hero-bottom"><div><p class="intro">{u['intro']}</p><p class="location">{icon("pin")}{u['location']}</p></div><a class="scroll-link" href="#work"><span>{u['scroll']}</span><span class="circle">{icon("arrow-down")}</span></a></div>
<details class="background"><summary><span class="with-icon">{icon("briefcase")}{u['background']}</span><span class="expand-icon" aria-hidden="true">+</span></summary><div class="details-content"><div class="background-content"><div><p class="bio">{E(c['aboutText'][0])}</p><ul class="jobs">{jobs}</ul></div><div><div class="skills">{skills}</div><div class="education">{schools}</div></div></div></div></details></section>
<section id="work" class="work shell" aria-labelledby="work-title"><div class="section-heading reveal"><h2 id="work-title">{u['work']}</h2><span>{project_count}</span></div><div class="projects">{''.join(project(p,c,u,i) for i,p in enumerate(c['projects']))}</div><div class="more-projects">{''.join(project(p,c,u,i+3) for i,p in enumerate(EXTRA_PROJECTS[key]))}</div></section>
<section id="contact" class="contact shell" aria-labelledby="contact-title"><div class="contact-inner reveal"><p class="contact-kicker">{u['say']}</p><h2 id="contact-title">{u['contact']}</h2><div class="contact-actions"><a class="email-button" href="mailto:hanssenbudi@gmail.com">{icon("mail")}{u['email']}</a><button class="copy-email" type="button" data-copy data-copied="{u['copied']}" data-failed="{u['failed']}" hidden>{icon("copy")}{u['copy']}</button><span class="copy-status" aria-live="polite" role="status"></span></div><a class="email-address" href="mailto:hanssenbudi@gmail.com">hanssenbudi@gmail.com</a></div><div class="contact-foot"><div><p>{u['links']}</p><div class="socials">{ext('https://github.com/cubelated','GitHub')}{ext('https://www.linkedin.com/in/hanssen-budisantoso-wijaya/','LinkedIn')}{ext('https://www.youtube.com/@cubelated','YouTube')}</div></div><a class="back" href="#home" aria-label="{u['back']}">{icon("arrow-up")}</a></div></section></main>
<footer class="footer shell"><span>© 2026 Hanssen Budisantoso Wijaya</span><span>{u['footer']}</span></footer></body></html>'''

def build():
    for key,c in CONTENT.items():
        path=ROOT/'dist'/c['path'].strip('/')/'index.html'
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(render(key,c), encoding='utf-8')
    urls = ''.join(f'<url><loc>{ORIGIN}{c["path"]}</loc></url>' for c in CONTENT.values())
    (ROOT / 'dist' / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + urls + '</urlset>\n', encoding='utf-8')
    (ROOT / 'dist' / 'robots.txt').write_text(
        f'User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n', encoding='utf-8')
    print('Built English and Traditional Chinese: Home / Work / Contact.')
