from pathlib import Path
import json,re,unicodedata,html
from urllib.parse import quote
R=Path(__file__).resolve().parents[1];D=R/'dist'
def norm(s):return ''.join(c for c in unicodedata.normalize('NFD',s) if not unicodedata.combining(c)).lower()
profiles={norm(x['name']):x['url'] for x in json.loads((R/'source/faculty-cvlac.json').read_text())}
url='https://www.youtube.com/watch?v=9gAK0wLzbLM'
embed='https://www.youtube-nocookie.com/embed/9gAK0wLzbLM'
for p in D.rglob('*.html'):
 s=p.read_text();en=p.parent.name=='en';prefix='../' if en else ''
 if 'class="brandmark"' not in s:
  s=s.replace('<span class="brand-name">','<span class="brandmark">OAN<span>1803</span></span><span class="brand-name">',1)
 if p.name=='isleia.html':
  img=f'<figure class="isle-identity"><img src="{prefix}assets/isleia-identidad.png" alt="isleIA — '+('the OAN’s AI' if en else 'la IA del OAN')+'" loading="lazy"></figure>'
  s=re.sub(r'<div class="isle-art".*?</small></div>',lambda m:img,s,count=1)
 if p.name=='profesores.html':
  def person(m):
   block=m[0];name=re.search('<h3>(.*?)</h3>',block)[1];u=profiles[norm(name)]
   if 'generarCurriculoCv' not in block:
    label='CvLAC — academic CV' if en else 'CvLAC — hoja de vida'
    block=block.replace('</div></article>',f'<br><a href="{html.escape(u,quote=True)}" target="_blank" rel="noopener">{label} ↗</a></div></article>')
   return block
  s=re.sub(r'<article class="person">.*?</article>',person,s)
 if p.name=='patrimonio.html':
  title='Virtual tour of the historic Observatory' if en else 'Recorrido virtual por la sede histórica'
  caption='Universidad Nacional de Colombia · Bogotá Campus. If playback is unavailable, open the video on YouTube.' if en else 'Universidad Nacional de Colombia · Sede Bogotá. Si no puedes reproducirlo aquí, abre el video en YouTube.'
  label='Watch the virtual tour on YouTube' if en else 'Ver recorrido virtual en YouTube'
  figure=f'<figure class="heritage-tour"><div class="facebook-video"><iframe src="{html.escape(embed,quote=True)}" title="{title}" loading="lazy" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share; fullscreen" allowfullscreen></iframe></div><figcaption>{caption} <a href="{url}" target="_blank" rel="noopener">{label} ↗</a></figcaption></figure>'
  s=re.sub(r'<figure><img class="wide-image"[^>]*historic.jpg.*?</figure>',lambda m:figure,s,count=1)
 p.write_text(s)
