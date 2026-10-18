# Hunter project website

A small static project page for a private, local-first media discovery companion. No framework, JavaScript, external fonts, analytics or runtime API calls.

**Local draft only. Do not publish yet.** See [REVIEW.md](REVIEW.md) for the content review, privacy boundary and validation limits. Nothing has been pushed or deployed by this implementation.

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
- `PUBLICATION.md`: publication steps to carry out only after approval.

The owner confirmed the supplied captures have been masked appropriately, renamed in-image and fitted with device frames, and contain no private addresses or credentials. All 12 are now included under descriptive filenames in `site/assets/`, byte-for-byte identical to the supplied versions. The hero uses macOS/iOS Movies captures; a responsive gallery covers the collection, with six additional captures under “More from Hunter”. Images below the hero load lazily. No further blur or image alterations were applied. Do not serve the workspace root.

## Licensing

No source licence has been applied. MIT is proposed for the original website code, subject to the owner's approval. A future licence must exclude provider trademarks/logos and third-party imagery. No licence or changes apply to the private application.

The public-facing name is **Hunter**. The private application name remains unchanged. The existing local folder, Git remote and proposed Pages path retain `plex-hunter-site`; no remote rename has been performed.
