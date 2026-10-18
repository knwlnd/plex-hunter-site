# GitHub Pages deployment

The site is ready for standard branch deployment, with **index.html at the root of main**. No build process or custom GitHub Actions workflow is required.

## Repository configuration

Repository: `knwlnd/plex-hunter-site`

In **Settings → Pages → Build and deployment** choose:

- **Source:** Deploy from a branch
- **Branch:** main
- **Folder:** / (root)

Read-only checks on 18 October 2026 confirmed that these settings were already selected and HTTPS was enforced. The private application repository, `knwlnd/plex-hunter`, was confirmed private. No GitHub settings were changed during this work.

## Publish

1. Run `python3 scripts/check.py` locally.
2. Commit the root-layout changes, including deletion of the custom workflow and old `site/` layout, then push `main`.
3. GitHub Pages will deploy automatically using its standard branch publishing process.
4. Open https://knwlnd.github.io/plex-hunter-site/ and confirm that the root shows Hunter, including its screenshots and styling.

No separate Run workflow action is needed. No custom build script, package installation, secrets or deployment branch is required. The root `.nojekyll` file keeps this an ordinary static website.

## Public files

The website comprises 18 files: root HTML, CSS, `.nojekyll`, and 15 files in `images/`. Documentation and the local validation script are also intentionally part of the public repository and may be accessed through branch hosting. The workspace `assets/`, previous `dist/`, local review folder and OS files remain ignored. Never force-add ignored source material.

The owner reviewed the proposed site and supplied the masked screenshots. Final checks after the push: navigation, screenshots, “More from Hunter”, provider links, favicon/social image, desktop/mobile layout, keyboard focus and zoom. Do not change the private application or production MusicBrainz configuration as part of website publishing.

Future changes publish when pushed to `main`.

Reference: [GitHub Pages publishing source configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
