# Hunter project website

A small static project page for a private, local-first media discovery companion. No framework, JavaScript, external fonts, analytics or runtime API calls.

**Deployment prepared.** The owner has approved the proposed site. See [PUBLICATION.md](PUBLICATION.md) for the manual GitHub Pages workflow and source setting. Pages is currently enabled from the repository root; this preparation has not changed its settings or triggered a deployment. See [REVIEW.md](REVIEW.md) for validation and attribution details.

## Preview

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8000/ in a browser. No installation is needed. `dist/index.html` can also be opened directly.

## Layout

- `site/`: public HTML, CSS, favicon, original social image and official TMDB attribution logo, plus 12 owner-prepared screenshots.
- `scripts/`: dependency-free build and validation tools.
- `dist/`: generated publishable site (ignored).
- `assets/`: locally supplied, owner-prepared screenshots (ignored; selected public copies live in `site/assets/`).
- `REVIEW.md`: content, privacy, attribution and validation review.
- `.github/workflows/pages.yml`: manual Pages build, validation and deployment of `dist/` only.
- `PUBLICATION.md`: exact Pages source setting and deployment steps.

The owner confirmed the supplied captures have been masked appropriately, renamed in-image and fitted with device frames, and contain no private addresses or credentials. All 12 are now included under descriptive filenames in `site/assets/`, byte-for-byte identical to the supplied versions. The hero uses macOS/iOS Movies captures; a responsive gallery covers the collection, with six additional captures under “More from Hunter”. Images below the hero load lazily. No further blur or image alterations were applied. Do not serve the workspace root.

## Licensing

No source licence has been applied. MIT is proposed for the original website code, subject to the owner's approval. A future licence must exclude provider trademarks/logos and third-party imagery. No licence or changes apply to the private application.

The public-facing name is **Hunter**. The private application name remains unchanged. The existing local folder, Git remote and proposed Pages path retain `plex-hunter-site`; no remote rename has been performed.
