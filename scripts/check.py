#!/usr/bin/env python3
"""Static checks for the proposed public artifact; no third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
root = Path(__file__).resolve().parents[1] / 'dist'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.headings=[]; self.tags=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append(tag)
        if 'id' in a: self.ids.append(a['id'])
        if tag in ('a','link','img'):
            self.links.append(a.get('href',a.get('src','')))
        if tag == 'img': assert a.get('alt'), 'Image lacks alternative text'
        if tag in ('h1','h2','h3'): self.headings.append(tag)
p=Page();p.feed((root/'index.html').read_text())
assert len(p.ids)==len(set(p.ids)), 'Duplicate IDs'
assert p.headings.count('h1')==1
assert all(t in p.tags for t in ['main','nav','header','footer'])
assert 'script' not in p.tags
for href in p.links:
    url=urlsplit(href)
    if url.scheme:
        assert url.scheme=='https', 'Non-HTTPS external link'
    elif url.path:
        assert not url.path.startswith('/'), 'Root-relative URL breaks project hosting'
        assert (root/url.path).is_file(), 'Missing local resource: '+href
    if not url.scheme and url.fragment:
        assert url.fragment in p.ids, 'Missing anchor: '+href
patterns=[r'(?i)tailscale|\.ts\.net|localhost|127\.0\.0\.1',r'(?i)x-plex-token|api[_-]?key|authorization:|BEGIN .*PRIVATE KEY',r'\b(?:10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b',r'(?i)gh[pousr]_[A-Za-z0-9]{20,}',r'(?i)watched evidence|viewing history|owned in plex']
files=[f for f in root.rglob('*') if f.is_file()]
for f in files:
    assert f.suffix.lower() not in ('.jpeg','.jpg'), 'Unreviewed screenshot type'
    if f.suffix in ('.html','.css','.svg','.js','.json'):
        text=f.read_text()
        for pattern in patterns:
            assert not re.search(pattern,text), 'Privacy pattern in '+str(f.relative_to(root))
assert {str(f.relative_to(root)) for f in files}=={'.nojekyll','index.html','style.css','assets/favicon.svg','assets/social.png','assets/tmdb.svg'} | {
    'assets/'+name+'.png' for name in ['ios-movies', 'ios-new-noteworthy', 'ios-tv', 'ios-tv-library', 'ios-tv-exploring', 'macos-movies', 'macos-tv', 'macos-tv-library', 'macos-tv-library-more', 'macos-tv-exploring', 'macos-music-new-noteworthy', 'macos-music-library']
}
print(f'PASS: {len(files)} allowlisted files; local resources, anchor targets, semantic landmarks, image alternatives, HTTPS links and privacy patterns checked.')
print('External URL reachability and rendered accessibility/layout require separate review.')
print(f'Total uncompressed artifact: {sum(f.stat().st_size for f in files):,} bytes')
