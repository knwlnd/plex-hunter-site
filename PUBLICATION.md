# Deploy Hunter with GitHub Pages

## Current state

Read-only GitHub checks on 18 October 2026 confirmed:

- `knwlnd/plex-hunter-site` is public; its default branch is `main`.
- Pages is already enabled at https://knwlnd.github.io/plex-hunter-site/ with HTTPS enforced.
- Its current source is **Deploy from a branch → main → / (root)** (`build_type: legacy`, status `built`). This is the repository root, not the prepared website output in `dist/`.
- `knwlnd/plex-hunter` remains private. No application files or settings were changed.

The owner approved the proposed site visually and supplied the masked screenshots. Deployment preparation does not itself launch a new deployment. No push, GitHub setting change or workflow dispatch was performed in this step.

## Prepared workflow

[.github/workflows/pages.yml](.github/workflows/pages.yml) runs only when manually dispatched on `main`. It builds the static website, runs validation, uploads **only `dist/`**, then deploys through the `github-pages` environment. Pushes and pull requests do not trigger this workflow. No `gh-pages` branch is needed.

The build job has read-only repository permissions. Only the deployment job has Pages write and OIDC permissions. Credentials are not persisted by checkout. GitHub provides the deployment token automatically; no user secrets or API keys are needed.

## First deployment

1. Commit and push the deployment-preparation changes to `main` in `knwlnd/plex-hunter-site`. The existing branch-based Pages configuration may rebuild the repository root on that push; the prepared Hunter deployment starts only when the manual workflow runs after the source is switched.
2. In the website repository, open **Settings → Pages → Build and deployment → Source** and choose **GitHub Actions**. Do not choose the repository root or the private application repository.
3. Open **Actions → Deploy Hunter to GitHub Pages → Run workflow**, select **main**, and run it.
4. Wait for both `build` and `deploy` jobs to pass. Open the URL shown by the deployment environment: https://knwlnd.github.io/plex-hunter-site/.

If using the GitHub CLI after the workflow has been pushed, the corresponding source-setting and manual deployment commands are:

```sh
gh api --method PUT repos/knwlnd/plex-hunter-site/pages -f build_type=workflow
gh workflow run pages.yml --repo knwlnd/plex-hunter-site --ref main
gh run list --repo knwlnd/plex-hunter-site --workflow pages.yml --limit 5
```

To avoid another root-based build during the first push, switch Pages to GitHub Actions immediately before pushing the workflow, then run it afterwards. Changing the source alone does not run this manual workflow. No repository visibility changes are needed.

## Local checks

```sh
python3 scripts/build.py
python3 scripts/check.py
```

The reviewed output has 18 files: the HTML, CSS, favicon, social image, TMDB logo, `.nojekyll` and 12 owner-prepared screenshots. The ignored workspace `assets/`, scripts, review documents and Git metadata are not uploaded as the site artifact.

## Verify the deployment

- Confirm the public root shows Hunter rather than the repository README.
- Check navigation, the hero, screenshots, “More from Hunter”, provider links, favicon and social metadata.
- Check desktop/mobile layouts, keyboard focus and zoom in your browsers.
- Inspect the workflow artifact: only the 18 expected public files should be present.
- Leave the private application, production configuration and MusicBrainz User-Agent unchanged. After the public page is validated, its actual URL can be recommended separately as the contact URL.

Future releases use the same manual workflow after source changes have been pushed to `main`. No automatic publishing has been added.

Reference: [GitHub’s custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
