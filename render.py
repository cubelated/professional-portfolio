"""Static, bilingual portfolio. Native disclosures keep every detail accessible."""
from content import CONTENT, ROOT, ORIGIN, E
import json
import base64
from icons import icon
from additional_projects import EXTRA_PROJECTS
from company_projects import COMPANY_PROJECTS

UI = {
 'en': {'nav':['Home','Work','Contact'],'hello':'Hi, I’m Hanssen, also known as Cubelated.','hero':'Software with<br><span>purpose.</span>','intro':'I build mobile apps, web platforms, and connected systems that make everyday work feel simpler.','location':'Software Engineer · Full-Stack, Mobile Apps & System Integration','scroll':'Explore selected work','background':'A little about me','work':'Selected work','selected':'03 projects','open':'Explore project','close':'Close details','contact':'Good things start<br>with a <span>conversation.</span>','say':'Have a project in mind or a role to fill?','email':'Email me','copy':'Copy email','copied':'Email copied','failed':'Couldn’t copy. Use the email link.','links':'Elsewhere','footer':'Built with purpose.','back':'Back to top','renew':'Keep what matters.<br>Never miss a date.','selah':'Pause.<br>Pray.<br><i>Praise.</i>','planner':'People.<br>Plans.<br><span>Connected.</span>','renewSubtitle':'Life admin, simplified.','selahSubtitle':'A little space for stillness.','plannerSubtitle':'A clearer way to coordinate.','more':'Experience & skills'},
 'zh': {'nav':['首頁','作品','聯絡'],'hello':'你好，我是黃晟旺 Hanssen，也叫 Cubelated。','hero':'用軟體，<br><span>解決真實問題。</span>','intro':'打造行動應用、網頁平台與整合系統，讓日常工作少一點繁瑣。','location':'軟體工程師・全端開發、行動應用與系統整合','scroll':'探索精選作品','background':'多認識我一點','work':'精選作品','selected':'03 個專案','open':'探索專案','close':'收起內容','contact':'好的合作，<br>從<span>對話</span>開始。','say':'正在規劃新專案，或尋找工程夥伴嗎？','email':'寄信給我','copy':'複製信箱','copied':'已複製信箱','failed':'無法複製，請使用信箱連結。','links':'也可以在這裡找到我','footer':'用心打造。','back':'回到頂端','renew':'重要的事，<br>不再錯過期限。','selah':'停下。<br>禱告。<br><i>讚美。</i>','planner':'團隊。<br>安排。<br><span>連結。</span>','renewSubtitle':'把生活瑣事，變得簡單。','selahSubtitle':'為安靜，留一點空間。','plannerSubtitle':'更清楚的團隊協調方式。','more':'經歷與技能'}
}

SERVICES = {
    'en': {
        'heading': 'Business digital transformation',
        'intro': 'I help businesses turn manual work into connected digital workflows, from customer-facing products to the tools teams use every day.',
        'items': ['Websites & web apps', 'Mobile apps', 'API & system integrations', 'Workflow automation', 'Internal tools & dashboards'],
    },
    'zh': {
        'heading': '企業數位轉型',
        'intro': '協助企業將人工流程轉化為串連整合的數位工作流程，從面向客戶的產品，到團隊每天使用的工具。',
        'items': ['網站與網頁應用', '行動應用開發', 'API 與系統整合', '工作流程自動化', '內部工具與儀表板'],
    },
}

def ext(url,label):
    symbol = 'github' if 'github.com' in url else 'linkedin' if 'linkedin.com' in url else 'youtube' if 'youtu' in url else 'globe'
    return f'<a href="{E(url)}" target="_blank" rel="noopener noreferrer">{icon(symbol)}<span>{E(label)}</span>{icon("external")}</a>'

def extra_media(p,c):
    isen = c['lang']=='en'
    media = []
    if p.get('coverMedia'):
        file,width,height,caption = p['coverMedia']
        media.append(media_image('/media/' + file + '.webp', width, height, caption, p.get('coverOriginal')))
    if p.get('videoEmbed'):
        label = 'Watch playlist' if p['slug']=='learnalgo' and isen else '觀看播放清單' if p['slug']=='learnalgo' else 'Watch project video' if isen else '觀看專案影片'
        thumbnail = p.get('videoThumbnail') or ('/media/' + p['media'][0][0] + '.webp' if p.get('media') else '')
        preview = f'<img class="video-thumbnail" src="{E(thumbnail)}" alt="" width="480" height="360" loading="lazy" decoding="async" data-video-thumbnail>' if thumbnail else ''
        media.append(f'<div class="video-embed"><a class="video-launch" href="{E(p["url"])}" target="_blank" rel="noopener noreferrer" data-embed="{E(p["videoEmbed"])}" data-video-title="{E(p["name"])} — {label}">{preview}{icon("youtube")}<span>{label}<small>YouTube · {E(p["name"])}</small></span>{icon("play")}</a></div>')
    for file,w,h,caption in p.get('media',[]):
        full = 'View full-size image' if isen else '查看完整尺寸圖片'
        media.append(f'<figure class="project-media"><a href="/media/{file}.webp" target="_blank" rel="noopener noreferrer" aria-label="{full}: {E(caption)}"><img src="/media/{file}.webp" alt="{E(caption)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a><figcaption>{E(caption)} {icon("external")}</figcaption></figure>')
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

def media_image(src, width, height, caption, full_src=None):
    return f'<figure class="project-media"><a href="{E(full_src or src)}" target="_blank" rel="noopener noreferrer"><img src="{E(src)}" width="{width}" height="{height}" loading="lazy" decoding="async" alt="{E(caption)}"></a><figcaption>{E(caption)}</figcaption></figure>'

def project_media(slug,m,c):
    if slug == 'renewables':
        return [media_image('/renewables.webp',1080,1920,c['imageAlt'])]
    if slug == 'selah':
        return [media_image('/media/selah-home.webp',600,1286,m['home']),
            f'<figure class="project-media session-demo"><video controls playsinline preload="none" width="720" height="1544" poster="/media/selah-poster.webp" aria-label="{m["video"]}"><source src="/media/selah-walkthrough.mp4" type="video/mp4"><a href="/media/selah-walkthrough.mp4">{m["fallback"]}</a></video><figcaption>{m["videoCaption"]}</figcaption></figure>']
    if slug == 'ifgf-planner':
        return [media_image('/media/planner-dashboard.webp',1898,870,m['dashboard']),
                media_image('/media/planner-schedule.webp',1900,869,m['schedule'])]
    return []

def media_carousel(slides, p, c):
    if not slides:
        return ''
    en = c['lang']=='en'
    slug = p.get('slug',p.get('repo'))
    label = p['name'] + (' project media' if en else ' 專案媒體')
    slide_label = 'slide' if en else '投影片'
    items = ''.join(f'<div class="media-slide" role="group" aria-roledescription="{slide_label}" aria-label="{i+1} / {len(slides)}">{slide}</div>' for i,slide in enumerate(slides))
    controls = ''
    if len(slides)>1:
        previous = 'Previous media' if en else '上一張'
        following = 'Next media' if en else '下一張'
        controls = f'<div class="carousel-controls" hidden><button type="button" data-carousel-prev aria-label="{previous}" aria-controls="media-{slug}">{icon("chevron")}</button><span class="carousel-status" aria-live="polite" aria-atomic="true">1 / {len(slides)}</span><button type="button" data-carousel-next aria-label="{following}" aria-controls="media-{slug}">{icon("chevron")}</button></div>'
    return f'<section class="media-carousel" aria-label="{E(label)}" aria-roledescription="carousel"><div class="carousel-viewport" id="media-{slug}" tabindex="0" aria-label="{E(label)}">{items}</div>{controls}</section>'

def project_cover(p,c,u,index):
    slug=p.get('slug',p.get('repo'))
    m=MEDIA['en' if c['lang']=='en' else 'zh']
    typ = {'renewables':'renew', 'selah':'selah', 'ifgf-planner':'planner'}.get(slug)
    logo_file = {'renewables':'renewables-logo', 'selah':'selah-logo'}.get(slug) or p.get('logo')
    brand = f'<img class="project-logo" src="/media/{logo_file}.webp" width="32" height="32" alt="" loading="lazy">' if logo_file else icon(p.get('icon','briefcase'))
    if logo_file and p.get('logoWordmark'):
        tone = ' logo-monochrome' if p.get('logoMonochrome') else ''
        brand = f'<img class="project-logo project-wordmark{tone}" src="/media/{logo_file}.webp" width="90" height="28" alt="" loading="lazy" decoding="async">'
    if p.get('logoSrc'):
        brand = f'<img class="project-logo company-logo" src="{E(p["logoSrc"])}" width="90" height="32" alt="" loading="lazy" decoding="async">'
    top = f'<span class="cover-top"><span class="cover-brand">{brand}{E(p["name"])}</span><span>{index+1:02d}</span></span>'
    if typ:
        cover_words = u[typ].replace('<br>', ' ') if typ == 'planner' else u[typ]
        visual = f'<span class="cover-words">{cover_words}</span>'
        if slug == 'renewables':
            visual += f'<img class="renew-screen" src="/renewables.webp" alt="{E(c["imageAlt"])}" width="1080" height="1920" loading="lazy" decoding="async">'
        elif slug == 'selah':
            visual += f'<img class="selah-screen" src="/media/selah-home.webp" alt="{m["home"]}" width="600" height="1286" loading="lazy" decoding="async">'
        else:
            visual += f'<img class="planner-screen" src="/media/planner-dashboard.webp" alt="{m["dashboard"]}" width="1898" height="870" loading="lazy" decoding="async">'
        cover = f'<span class="cover {typ}">{top}{visual}<span class="cover-bottom">{E(u[typ+"Subtitle"])}</span></span>'
    else:
        if p.get('coverMedia') or p.get('media'):
            file,width,height,caption = p.get('coverMedia') or p['media'][0]
            visual = f'<img class="showcase-preview" src="/media/{file}.webp" alt="{E(caption)}" width="{width}" height="{height}" loading="lazy" decoding="async">'
        else:
            visual = '<span class="showcase-stack">' + ''.join(f'<span>{E(tag)}</span>' for tag in p['tags'][:3]) + '</span>'
        cover = f'<span class="cover showcase-cover showcase-{slug}">{top}<span class="showcase-tagline">{E(p["tagline"])}</span>{visual}<span class="showcase-bottom">{E(p["category"])}</span></span>'
    destination = p.get('url') or ('https://github.com/cubelated/' + p['repo'] if p.get('repo') else '')
    if destination:
        label = ('Visit project' if c['lang']=='en' else '前往專案') + ': ' + p['name']
        return f'<a class="project-card-link" href="{E(destination)}" target="_blank" rel="noopener noreferrer" aria-label="{E(label)}">{cover}</a>'
    return f'<div class="project-card-static">{cover}</div>'

def project_group(p):
    if p.get('company') or p.get('type') in ('Internship project', '實習專案'):
        return 'professional'
    if p.get('type') in ('Personal product', 'Personal project', '個人產品', '個人專案'):
        return 'personal'
    return 'community'

def project(p,c,u,index):
    slug=p.get('slug',p.get('repo'))
    m=MEDIA['en' if c['lang']=='en' else 'zh']
    case=''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a,b in zip(c['caseLabels'],p['case']))
    links=(ext(p['url'],p.get('linkLabel',c['visit'])) if p.get('url') else '')+(ext('https://github.com/cubelated/'+p['repo'],c['code']) if p.get('repo') else '')
    if p.get('thesisUrl'):
        links += ext(p['thesisUrl'], 'Read thesis' if c['lang']=='en' else '閱讀論文')
    if p.get('documentUrl'):
        links += ext(p['documentUrl'], p['documentLabel'])
    thesis = ''
    if p.get('thesisTitle'):
        thesis_label = 'Master’s thesis' if c['lang']=='en' else '碩士論文'
        thesis = f'<div class="project-publication"><p class="publication-label">{thesis_label}</p><p class="publication-title">{E(p["thesisTitle"])}</p></div>'
    kind = 'company' if p.get('company') else 'personal' if p.get('type') in ('Personal product', 'Personal project', '個人產品', '個人專案') else 'other'
    attribution = f'<span class="project-company">{E(p["company"])}</span>' if p.get('company') else ''
    return f'''<article class="project showcase-project reveal" data-project-group="{project_group(p)}">{project_cover(p,c,u,index)}<details class="project-details" id="project-{slug}"><summary aria-label="{E(u['open'])}: {E(p['name'])}">
      <span class="project-meta"><span class="project-type project-type-{kind}">{E(p['type'])}</span>{attribution}</span>
      <span class="project-heading"><span><span class="project-name">{E(p['name'])}</span><span class="project-category">{E(p['category'])}</span></span><span class="expand-icon project-chevron" aria-hidden="true">{icon('chevron')}</span></span>
      <span class="summary-caption">{E(p['tagline'])}</span>
    </summary><div class="details-content"><div class="project-copy"><p>{E(p['description'])}</p>{thesis}<ul class="tags">{''.join(f'<li>{E(t)}</li>' for t in p['tags'])}</ul>{media_carousel(project_media(slug,m,c)+extra_media(p,c),p,c)}<dl>{case}</dl><div class="project-links">{links}</div></div></div></details></article>'''

def render(key,c):
    u=UI[key]; isen=key=='en'
    services = SERVICES[key]
    service_items = ''.join(f'<li>{E(item)}</li>' for item in services['items'])
    projects = c['projects'][:1] + COMPANY_PROJECTS[key] + c['projects'][1:] + EXTRA_PROJECTS[key]
    project_count = f'{len(projects):02d}' + (' projects' if isen else ' 個專案')
    filter_labels = [('all', 'All' if isen else '全部'),
                     ('professional', 'Professional' if isen else '專業工作'),
                     ('personal', 'Personal' if isen else '個人作品'),
                     ('community', 'Community & Research' if isen else '社群與研究')]
    filter_buttons = ''
    for group,label in filter_labels:
        count = len(projects) if group=='all' else sum(project_group(p)==group for p in projects)
        filter_buttons += f'<button type="button" data-project-filter="{group}" aria-pressed="{str(group=="all").lower()}" aria-controls="project-grid">{E(label)}<span class="filter-count">{count}</span></button>'
    filter_label = 'Filter projects' if isen else '篩選專案'
    count_label = '{visible} of {total} projects' if isen else '顯示 {visible} / {total} 個專案'
    more_label = 'View all {total} projects' if isen else '查看全部 {total} 個專案'
    fewer_label = 'Show fewer projects' if isen else '收合專案'
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
         'name': 'Hanssen Budisantoso Wijaya', 'alternateName': ['黃晟旺', 'Hanssen Budi', 'Cubelated'],
         'jobTitle': 'Software Engineer', 'url': ORIGIN + '/',
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
<link rel="icon" href="/logo.png?v=2" type="image/png"><link rel="apple-touch-icon" href="/logo.png?v=2"><link rel="stylesheet" href="/styles.css?v=18"><script src="/app.js?v=11" defer></script><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>
<body><a class="skip" href="#main">{c['skip']}</a><header class="header"><a href="#home" class="brand" aria-label="Hanssen Budisantoso Wijaya — {u['nav'][0]}"><img src="/logo.png" alt="" width="36" height="42"><span>Hanssen Budisantoso Wijaya</span></a><nav class="nav" aria-label="{'Main navigation' if isen else '主要導覽'}"><span class="nav-track" aria-hidden="true"></span>{navigation}</nav><label class="language-picker" for="site-language">{icon('globe')}<span class="sr-only">{'Language' if isen else '語言'}</span><select id="site-language" data-language aria-label="{'Language' if isen else '語言'}"><option value="/" lang="en" {'selected' if isen else ''}>English</option><option value="/zh-tw/" lang="zh-Hant" {'' if isen else 'selected'}>繁體中文</option></select>{icon('chevron')}</label><noscript><a href="{langlink}">{language}</a></noscript></header>
<main id="main"><section id="home" class="hero shell" aria-labelledby="hero-title"><div class="hero-visual"><img class="hero-banner" src="/media/banner.webp" alt="" width="1920" height="640" fetchpriority="high" decoding="async"><p class="hello">{u['hello']}</p><h1 id="hero-title">{u['hero']}</h1><div class="hero-bottom"><div><p class="intro">{u['intro']}</p><p class="location">{icon("briefcase")}<span>{E(u['location'])}</span></p></div><a class="scroll-link" href="#work"><span>{u['scroll']}</span><span class="circle">{icon("arrow-down")}</span></a></div></div>
<details class="background"><summary><span class="with-icon">{icon("user")}{u['background']}</span><span class="expand-icon" aria-hidden="true">+</span></summary><div class="details-content"><div class="background-content"><div><p class="bio">{E(c['aboutText'][0])}</p><ul class="jobs">{jobs}</ul></div><div><div class="skills">{skills}</div><div class="education">{schools}</div></div></div></div></details></section>
<section id="work" class="work shell" aria-labelledby="work-title"><div class="section-heading reveal"><h2 id="work-title">{u['work']}</h2><span data-project-count data-count-label="{E(count_label)}" role="status" aria-atomic="true">{project_count}</span></div><div class="project-filters" data-project-filters role="group" aria-label="{filter_label}" hidden>{filter_buttons}</div><div class="projects project-grid" id="project-grid" data-project-limit="6">{''.join(project(p,c,u,i) for i,p in enumerate(projects))}</div><div class="project-more" data-project-more hidden><button type="button" data-project-expand data-more-label="{E(more_label)}" data-fewer-label="{fewer_label}" aria-expanded="false" aria-controls="project-grid">{E(more_label.replace('{total}',str(len(projects))))}{icon('arrow-down')}</button></div></section>
<section id="contact" class="contact shell" aria-labelledby="contact-title"><div class="contact-inner reveal"><p class="contact-kicker">{u['say']}</p><h2 id="contact-title">{u['contact']}</h2><div class="contact-services"><h3>{services['heading']}</h3><p>{services['intro']}</p><ul class="service-list">{service_items}</ul></div><div class="contact-actions contact-links"><a class="email-button" href="mailto:hanssenbudi@gmail.com">{icon("mail")}<span>hanssenbudi@gmail.com</span></a><button class="copy-email" type="button" data-copy data-copied="{u['copied']}" data-failed="{u['failed']}" aria-label="{u['copy']}" title="{u['copy']}" hidden>{icon("copy")}</button>{ext('https://github.com/cubelated','GitHub')}{ext('https://www.linkedin.com/in/hanssen-budisantoso-wijaya/','LinkedIn')}{ext('https://www.youtube.com/@cubelated','YouTube')}<a class="back" href="#home" aria-label="{u['back']}">{icon("arrow-up")}</a></div></div></section></main>
<div class="snackbar" data-snackbar role="status" aria-live="polite" aria-atomic="true"><span class="snackbar-symbol" data-snackbar-success>{icon("check")}</span><span class="snackbar-symbol snackbar-symbol-error" data-snackbar-error hidden>{icon("alert-circle")}</span><span data-snackbar-message></span></div>
<footer class="footer shell"><span>© 2026 Hanssen Budisantoso Wijaya</span><span>{u['footer']}</span></footer></body></html>'''

def build():
    # Embed the untouched logo in a square viewport; meet preserves its ratio.
    logo = base64.b64encode((ROOT / 'dist' / 'logo.png').read_bytes()).decode('ascii')
    (ROOT / 'dist' / 'favicon.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">'
        '<image width="64" height="64" preserveAspectRatio="xMidYMid meet" '
        f'href="data:image/png;base64,{logo}"/></svg>\n', encoding='utf-8')
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
