"""Employer-owned projects, based on the user's project and career details."""

COMPANY_PROJECTS = {
    'en': [
        {
            'name': 'DCIMinside',
            'slug': 'dciminside',
            'logoSrc': '/media/hostinginside-logo.svg',
            'type': 'Company work',
            'company': 'HostingInside LTD',
            'category': 'Data center infrastructure',
            'tagline': 'Infrastructure visibility across three data centers.',
            'description': 'A company-owned data center infrastructure management application '
                           'I built during my time at HostingInside LTD.',
            'tags': ['DCIM', 'Infrastructure monitoring', 'Systems integration'],
            'case': [
                'Help teams monitor and manage data center infrastructure.',
                'Built the DCIM application and led a six-person engineering team as the '
                'platform expanded across three data centers.',
                'Infrastructure monitoring and connected systems in a production environment.',
            ],
            'icon': 'server',
        },
        {
            'name': 'CashierInside',
            'slug': 'cashierinside',
            'logoSrc': '/media/hostinginside-logo.svg',
            'coverMedia': ('cashierinside-poster', 1600, 724, 'CashierInside product page and cashier interface'),
            'coverOriginal': '/media/cashierinside-poster.png',
            'type': 'Company work',
            'company': 'HostingInside LTD',
            'category': 'Point-of-sale application',
            'tagline': 'Less waiting for the records that keep business moving.',
            'description': 'A company-owned cashier application I worked on at HostingInside LTD, '
                           'with a focus on POS data retrieval and performance.',
            'tags': ['POS', 'Data retrieval', 'Performance optimization'],
            'url': 'https://cashierinside.com/',
            'case': [
                'Keep point-of-sale workflows responsive as records grow.',
                'Optimized retrieval across tens to hundreds of thousands of records, '
                'reducing read times from 1–2 minutes to approximately 3 seconds.',
                'Improving production data access while supporting everyday cashier workflows.',
            ],
            'icon': 'briefcase',
        },
    ],
    'zh': [
        {
            'name': 'DCIMinside',
            'slug': 'dciminside',
            'logoSrc': '/media/hostinginside-logo.svg',
            'type': '公司專案',
            'company': 'HostingInside LTD',
            'category': '資料中心基礎架構',
            'tagline': '串連三座資料中心的基礎架構管理。',
            'description': '任職 HostingInside LTD 期間開發的資料中心基礎架構管理應用，產品由公司持有。',
            'tags': ['DCIM', '基礎架構監控', '系統整合'],
            'case': [
                '協助團隊監控與管理資料中心基礎架構。',
                '開發 DCIM 應用，並帶領六人工程團隊，將平台擴展至三座資料中心。',
                '正式環境中的基礎架構監控與系統整合。',
            ],
            'icon': 'server',
        },
        {
            'name': 'CashierInside',
            'slug': 'cashierinside',
            'logoSrc': '/media/hostinginside-logo.svg',
            'coverMedia': ('cashierinside-poster', 1600, 724, 'CashierInside 產品頁與收銀介面'),
            'coverOriginal': '/media/cashierinside-poster.png',
            'type': '公司專案',
            'company': 'HostingInside LTD',
            'category': '收銀應用',
            'tagline': '讓日常營運需要的資料，不再久候。',
            'description': '任職 HostingInside LTD 期間參與開發的收銀應用，專注 POS 資料讀取與效能優化，產品由公司持有。',
            'tags': ['POS', '資料讀取', '效能優化'],
            'url': 'https://cashierinside.com/',
            'case': [
                '隨著資料量成長，維持收銀流程的回應速度。',
                '優化數萬至數十萬筆資料的讀取流程，將耗時從 1–2 分鐘縮短至約 3 秒。',
                '改善正式環境的資料存取效能，支援日常收銀作業。',
            ],
            'icon': 'briefcase',
        },
    ],
}
