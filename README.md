# Hunter

A static project website for a private, local-first media discovery companion. No framework, JavaScript, external fonts, analytics or runtime API calls.

## GitHub Pages

Publish directly from **main / (root)** using **Settings → Pages → Build and deployment → Source: Deploy from a branch**. No build step, custom Actions workflow or separate deployment branch is needed.

Website: https://knwlnd.github.io/plex-hunter-site/

- `index.html`, `style.css`, `.nojekyll`: the website at the repository root.
- `images/`: favicon, sharing image, TMDB attribution logo and 12 owner-prepared screenshots.
- `scripts/check.py`: optional local validation; not needed by GitHub Pages.
- `PUBLICATION.md`: deployment instructions.
- `REVIEW.md`: content, attribution and validation review.

Open `index.html` directly in a browser to preview. Run `python3 scripts/check.py` to validate the website files and links.

The workspace `assets/` folder is ignored and is not part of the Git repository. The prepared public screenshot copies are in `images/`. Their masking and device frames are unchanged from the owner-supplied files.

## Licensing

No source licence has been applied. MIT is proposed for original website code, subject to approval, with provider branding and third-party imagery excluded. The private application and its name are unchanged; the public-facing name is Hunter.
