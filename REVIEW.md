# Website review — 18 October 2026

**Recommendation: CONDITIONAL GO, pending owner content approval and browser verification.** The public-facing name is now Hunter, as requested by the owner. The private application is not being renamed or distributed. The owner will complete desktop/mobile browser verification. No public repository was created, no push was performed and Pages was not enabled.

## Content and public claims

The page introduces a private, local-first Plex companion and accurately lists the supplied Movies, TV and Music discovery categories. It explains library → metadata → recommendations → feedback, understandable recommendation reasons, private deployment, controlled playlist changes and no automatic acquisition. It states that this is an actively used personal project without a public download or hosted service. It makes no operational historical-intelligence claims. Contact points only to the approved GitHub profile.

The hero now shows the owner-prepared macOS and iOS Movies captures. The screenshot section includes all 12 supplied captures across macOS and iOS, with six additional images behind a native disclosure. Captions identify them as actual application captures with selected details masked and device frames added. No screenshot is generated or altered. The social graphic contains only original typography.

## Privacy and security

The owner replaced the original screenshots with 12 prepared PNGs and confirmed that they contain no private data, addresses or credentials, that “Plex” has been removed from the application-name label, and that masking and device bezels have been added. These prepared images were visually inspected in a contact sheet. Their use in the proposed public site is within the owner's clarified scope; no additional redaction approval is being requested.

All 12 are copied byte-for-byte into `site/assets/` under descriptive filenames. Hash checks confirm exact matches. The original supplied files remain untouched in the ignored workspace `assets/` folder. CSS trims only transparent canvas margins in display; it is not used for privacy masking. Image metadata was inspected: screenshot EXIF contains only dimensions, alongside an embedded colour profile. The social PNG has no metadata.

The 18-file build contains the website and the owner-prepared captures; no detected credentials, private addresses or internal configuration appear in text source. The owner has reviewed the image content. No private application files were read or changed. The original reachable Git history contains one initial commit with only README.md and .gitattributes. The current checkout is separate from the private application repository. Private repository visibility was not independently inspected and must be confirmed at release time.

Automated pattern checks are a useful check, not a guarantee against every possible secret. The new source and generated artifact were also reviewed by content. The build is an explicit publication boundary, and refuses unexpected output files. No remote code, fonts, trackers or scripts run in visitors' browsers; provider and GitHub links are ordinary outbound navigation.

## Provider attribution and public branding

- **Plex:** the public page now uses **Hunter** throughout its branding and metadata, including the social card. Plex appears only as the platform the project works with and in the independence/ownership acknowledgement. The private application name remains unchanged and the application is not offered for distribution. The [official guidelines](https://www.plex.tv/en-au/about/privacy-legal/plex-trademarks-and-guidelines/) informed the external-name change; this report does not claim trademark clearance or a negotiated licence. No Plex logo is used. Existing local paths and the proposed repository URL remain unchanged; no remote was renamed.
- **TMDB:** [official FAQ](https://developer.themoviedb.org/docs/faq) requires an approved logo and a non-endorsement notice. Both appear in the credits. The official unmodified SVG was downloaded from the [logo/attribution page](https://www.themoviedb.org/about/logos-attribution). It is linked to TMDB, smaller than the project identity, rendered in its original aspect ratio, and served locally. This website makes no API calls. Its screenshots include application metadata and poster art; these remain third-party material, acknowledged through the credits.
- **MusicBrainz:** [data licensing](https://musicbrainz.org/doc/About/Data_License) distinguishes CC0 core data from supplementary data under CC BY-NC-SA 3.0. The page acknowledges MusicBrainz. Music screenshots include application metadata; provider terms continue to apply to embedded data.
- **Cover Art Archive:** the [official project policy](https://musicbrainz.org/doc/Cover_Art_Archive) asks users to respect artist/label rights. Availability through the archive is not blanket permission to republish artwork. The page acknowledges the MusicBrainz/Internet Archive collaboration and includes album artwork within the owner-prepared music screenshots. No CAA logo is copied.
- **Source licence:** MIT is recommended for original website code only, subject to approval. No licence was automatically added. Provider branding and screenshots/artwork need explicit exclusions and their own rights review. The private application is unaffected.

Sources checked 18 October 2026. Plex and TMDB branding pages were retrieved directly after web-reader access restrictions; no third-party branding copies were used.

## Validation results and limits

- PASS: dependency-free build and 18-file generated allowlist (HTML, CSS, favicon, social PNG, TMDB SVG, .nojekyll and 12 prepared screenshots).
- PASS: all local resource paths exist, no root-relative paths, fragment links resolve, one h1, semantic landmarks, image alternatives, external links use HTTPS.
- PASS: artifact privacy-pattern scan and manual text review; only owner-prepared screenshot copies included; original unredacted screenshots absent from artifact and reachable Git history.
- PREVIOUS BASELINE: the initial site and its assets returned HTTP 200 in local preview. The new screenshot paths pass file-resolution checks; their rendered appearance remains for owner browser review.
- SOURCE REVIEW: responsive media queries cover desktop, tablet and mobile; no fixed-width content column, small-screen navigation wraps, reduced motion disables smooth scrolling, skip link and visible focus styles are present. Native links provide keyboard operation without JavaScript. These are implementation checks, not rendered accessibility certification.
- NOT VERIFIED: rendered layout at desktop/mobile widths, overflow, zoom, keyboard operation and screen-reader behaviour. Browser tool reported no browser connection, and native Chrome access was not approved. No claim of passed visual or automated accessibility testing is made. Complete manual review before publication.
- NOT VERIFIED: every external link's eventual destination; official provider references were researched, but no complete live link crawl was performed. Recheck at publication. Canonical/social URLs are prospective, not an assertion of a live deployment.

The site has no framework build, package installation or JavaScript tests to run. The owner will complete browser validation; final public content approval remains open. No production configuration, MusicBrainz User-Agent or application deployment was changed.

## Screenshot integration validation

All 12 prepared source files match their public copies by SHA-256. Each image has descriptive alternative text and explicit source dimensions. The hero loads its main screenshot with high priority; other images use native lazy loading. The gallery and “More from Hunter” disclosure require no JavaScript, and the disclosure has visible keyboard focus styling. CSS uses the transparent-canvas bounds to display the devices at a useful size without modifying any screenshot pixels. The build totals approximately 6.77 MB, mostly screenshots; later images are deferred by native browser loading. Browser rendering will be verified by the owner, as requested.
