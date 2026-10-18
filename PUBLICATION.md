# GitHub Pages publication — after approval only

Target: `knwlnd/plex-hunter-site`, a separate website repository. Do not change the private application repository. The checkout already has an origin pointing to this target; that does not establish its current existence, visibility or Pages status. This task did not change any remote settings.

## Release gate

1. Review the public-facing **Hunter** branding. The private application name remains unchanged. The current proposed Pages path retains the existing repository slug; if a new public repository name is chosen, update canonical and social URLs before release.
2. Approve the website content, any edited screenshot selections, provider credits and proposed source licence (or approve retaining no licence). Review any remaining Plex references and applicable attribution wording without claiming a licence that has not been granted.
3. Review `git status`, every file to be committed and all reachable Git history. Never force-add `assets/` or the ignored local review folder.
4. Run `python3 scripts/build.py` and `python3 scripts/check.py`. Inspect all 18 generated files. Verify desktop and mobile rendering, keyboard navigation, zoom, contrast and external links manually.
5. Independently confirm the application repository remains private before publication. Its settings were not accessed in this task.

## Exact hosting setup

After explicit content/privacy and publication approval, use the existing dedicated site repository if it exists; otherwise create `knwlnd/plex-hunter-site` as the dedicated public repository. Never create or replace `knwlnd/plex-hunter`.

Use a dedicated `gh-pages` branch containing **only the contents of `dist/` at its root**. Prepare that branch in a separate checkout, review its file list, then push it after approval. Keep source on `main`. Do not use the workspace root as a Pages publishing source.

In the site repository: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: gh-pages → Folder: / (root) → Save**. Keep `.nojekyll` in the published root. Enable HTTPS if offered. Do not add a custom domain.

Expected address (not currently verified live): https://knwlnd.github.io/plex-hunter-site/

This branch-based setup needs no Actions workflow or build dependencies. GitHub documents [publishing source configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## After deployment

- Verify the actual public URL returns success and the page, CSS, screenshots, favicon, social image and TMDB logo load under the repository path.
- Check all anchor and provider links, desktop and mobile widths, keyboard focus, reduced motion and 200% zoom.
- Inspect the published branch and browser network requests. Only the 18 reviewed files should be served; no private assets, API requests or application links.
- Verify the private application repository is still private and unchanged.
- Only after the public page is live and validated, recommend using its actual URL as the MusicBrainz User-Agent contact URL. Do not change production configuration as part of this website task.
