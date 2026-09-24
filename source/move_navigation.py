"""Place the two new sections alongside eSPECTRA in every language."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for p in (root/'dist').rglob('*.html'):
 s=p.read_text();en=p.parent.name=='en'
 old=re.search(r'<div class="new-tabs">(.*?)</div>',s)
 if old:
  language=re.search(r'<nav class="language-switch".*?</nav>',old.group(1)).group(0)
  s=s[:old.start()]+s[old.end():]
 else:
  language=re.search(r'<nav class="language-switch".*?</nav>',s).group(0)
 def update(m):
  bar=re.sub(r'<nav class="language-switch".*?</nav>','',m.group(1))
  bar=re.sub(r'<a\b[^>]*href="(?:jueves|isleia)\.html"[^>]*>.*?</a>','',bar)
  title='Thursdays under the Stars' if en else 'Jueves bajo las estrellas'
  links=f'<a href="jueves.html">{title}</a><a href="isleia.html">IsleIA</a>'
  bar=bar.replace('<a href="espectra.html">eSPECTRA</a>','<a href="espectra.html">eSPECTRA</a>'+links)
  return '<div class="utility-nav">'+bar+language+'</div>'
 s=re.sub(r'<div class="utility-nav">(.*?)</div>',update,s,count=1)
 p.write_text(s)
