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

The current site uses Sites hosting. Its configuration is in `.openai/hosting.json`. To use another static host, publish the complete `dist/` directory and update `ORIGIN` in `content.py` before rebuilding. Repository storage does not automatically enable GitHub Pages or change the site's audience.

## Checks

```sh
python3 build.py
node --check dist/app.js
```

Manually review both languages at mobile, tablet, and desktop widths; verify keyboard focus, rapid disclosure toggles, hover transitions, header navigation, and media playback. This environment does not provide a compatible browser preview for this static project, so source checks are not a substitute for visual browser QA.

## Assets and attribution

Project identity, copy, logos, screenshots, and videos belong to their respective owners. Third-party icon attribution is in `THIRD_PARTY_NOTICES.md`. No additional open-source license is granted by this repository.
