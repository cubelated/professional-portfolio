# Hanssen Budisantoso Wijaya — Portfolio

A lightweight professional portfolio with English and Traditional Chinese pages, project media, and animated progressive disclosure.

## Run locally

Requires Python 3.10 or newer. No third-party Python or JavaScript packages are required.

```sh
python3 build.py
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000/` for English or `http://localhost:8000/zh-tw/` for Traditional Chinese. Serve the site at the domain root because asset and language URLs are root-relative.

## Edit

| File | Purpose |
| --- | --- |
| `content.py` | Profile, experience, and featured projects in both languages |
| `additional_projects.py` | Additional projects and YouTube media |
| `render.py` | HTML templates, navigation, and short interface copy |
| `icons.py` | Inline SVG icon helpers |
| `dist/styles.css` | Responsive layouts, spacing, and transition timing |
| `dist/app.js` | Navigation, disclosures, reveals, language changes, and media playback |
| `dist/media/` | Project images, logos, and video |

Run `python3 build.py` after changing Python source. The HTML files are generated; edit their templates instead. CSS, JavaScript, and media in `dist/` are source assets, so do not delete this directory as a build cleanup step. Increment their query versions in `render.py` when publishing changes.

## Interaction details

- Three primary destinations: Home, Work, Contact.
- English is the default; the language dropdown preserves the active section.
- Native details and direct media links keep core content available without JavaScript.
- YouTube embeds load only after a click and are removed when their project closes.
- Motion timings are defined as CSS variables: 160 ms feedback, 240 ms hover, 280 ms disclosure, 380 ms reveal, and 480 ms navigation scroll.
- Disclosure motion can reverse on repeated clicks. Scroll motion yields to wheel, touch, and keyboard input.

## Publish

The production domain is `https://cubelated.com`. Cloudflare should build with `python3 build.py` and publish the complete `dist/` directory. For Workers Static Assets, the deploy command is `npx wrangler deploy --assets ./dist`. Keep the existing Cloudflare Worker name and Git integration. The `.openai/hosting.json` file belongs to the original Sites deployment and is not Cloudflare configuration.

## SEO and indexing

`ORIGIN` in `content.py` is the single source for canonical URLs, language alternatives, structured data, sharing metadata, `robots.txt`, and `sitemap.xml`. Rebuild after changing it. Each language has its own canonical URL; home/work/contact fragments are sections, not separate indexable pages.

After Cloudflare deploys:

- Verify `/` and `/zh-tw/` return HTTP 200 with the new metadata, and a nonexistent URL returns HTTP 404. Keep SPA fallback disabled for this static bilingual site.
- Use Cloudflare domain redirect rules for HTTP and `www` to `https://cubelated.com`, preserving paths and query strings. Do not use a catch-all path redirect that sends the Chinese page to the English homepage.
- Verify the `cubelated.com` Domain property in Google Search Console using its supplied DNS TXT record. Submit `https://cubelated.com/sitemap.xml`, then inspect both language URLs and request indexing. Account verification and submission are manual until account access is available.
- Check Google-selected canonical URLs and indexing coverage after recrawling. Canonical tags and structured data do not guarantee indexing, ranking, or rich results.
- Validate the JSON-LD with Schema.org Validator and Google's Rich Results Test. Social previews use the existing logo, not a generated cover image.

References: [Google canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [multilingual pages](https://developers.google.com/search/docs/specialty/international/localized-versions), [Cloudflare Workers Static Assets](https://developers.cloudflare.com/workers/static-assets/).

## Checks

```sh
python3 build.py
node --check dist/app.js
```

Manually review both languages at mobile, tablet, and desktop widths; verify keyboard focus, rapid disclosure toggles, hover transitions, header navigation, and media playback. This environment does not provide a compatible browser preview for this static project, so source checks are not a substitute for visual browser QA.

## Assets and attribution

Project identity, copy, logos, screenshots, and videos belong to their respective owners. Third-party icon attribution is in `THIRD_PARTY_NOTICES.md`. No additional open-source license is granted by this repository.
