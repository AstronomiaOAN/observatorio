"""Bilingual visual refresh and user-supplied institutional directory."""
from pathlib import Path
import re, json
D=Path(__file__).resolve().parents[1]/'dist'
roles=[
('Dirección Departamento','Department Director','Mario Armando Higuera Garzón','mahiguerag@unal.edu.co','11021','413-103'),
('Dirección Área Curricular','Curricular Area Director','Eduard Alexis Larrañaga Rubio','ealarranaga@unal.edu.co','11020','413-104'),
('Secretaría Departamento','Department Secretariat','Islena Bonilla','obsan_fcbog@unal.edu.co','11020','413-114'),
('Secretaría Posgrado','Graduate Secretariat','Islena Bonilla','obsan_fcbog@unal.edu.co','11020','413-114'),
('Sede Histórica','Historic Observatory','Gonzalo Jimenez Vargas','gjimenezv@unal.edu.co','',''),
('Coordinación de Investigación','Research Coordination','Santiago Vargas Domínguez','svargasd@unal.edu.co','11022','413-106'),
('Coordinación de Extensión','Outreach Coordination','Santiago Vargas Domínguez','svargasd@unal.edu.co','11022','413-106'),
('Acreditación','Accreditation','Eduard Alexis Larrañaga Rubio','ealarranaga@unal.edu.co','11020','413-104'),
('Coordinación de Laboratorios','Laboratory Coordination','Santiago Vargas Domínguez','svargasd@unal.edu.co','11022','413-106'),
('Comité de Ética','Ethics Committee','Santiago Vargas Domínguez','svargasd@unal.edu.co','11022','413-106')]
for p in D.rglob('*.html'):
 s=p.read_text(); en=p.parent.name=='en'; label='About us' if en else '¿Quiénes somos?'
 s=re.sub(r'(<a\b[^>]*href="profesores.html"[^>]*>)(Faculty|Profesores)(</a>)',lambda m:m[1]+label+m[3],s)
 if p.name=='profesores.html' and 'id="directorio"' not in s:
  old='The people behind the science' if en else 'Personas que hacen ciencia'
  s=s.replace(old,label).replace('>FACULTY<','>ABOUT US<').replace('>PROFESORES<','>QUIÉNES SOMOS<')
  s=s.replace('<div class="content"><section>', '<div class="subnav"><a href="#equipo">'+('Faculty' if en else 'Profesores')+'</a><a href="#directorio">'+('Directory' if en else 'Directorio')+'</a></div><div class="content"><section id="equipo"><h2>'+('Our faculty' if en else 'Nuestro equipo docente')+'</h2>',1)
  cards=''
  for es,eng,name,email,ext,office in roles:
   details=f'<dt>{"Email" if en else "Correo electrónico"}</dt><dd><a href="mailto:{email}">{email}</a></dd>'
   if ext: details+=f'<dt>{"Extension" if en else "Extensión"}</dt><dd>{ext}</dd><dt>{"Office" if en else "Oficina"}</dt><dd>{office}</dd>'
   cards+=f'<article class="directory-card"><h3>{eng if en else es}</h3><p class="directory-person">{name}</p><dl>{details}</dl></article>'
  directory='<section id="directorio"><p class="eyebrow">'+('CONTACTS' if en else 'CONTACTOS')+'</p><h2>'+('National Astronomical Observatory Directory' if en else 'Directorio del Observatorio Astronómico Nacional')+'</h2><div class="directory-grid">'+cards+'</div></section>'
  s=s.replace('</div></main>',directory+'</div></main>',1)
 p.write_text(s)
(D/'directorio.json').write_text(json.dumps([dict(zip(['cargo_es','cargo_en','nombre','correo','extension','oficina'],r)) for r in roles],ensure_ascii=False,indent=2))

# Existing documentary assets remain local and accompany related content.
for en in (False, True):
 root=D/'en' if en else D; prefix='../assets/' if en else 'assets/'
 def image(file,alt,caption,cls='editorial-image'):
  return f'<figure class="{cls}"><img src="{prefix}{file}" alt="{alt}" loading="lazy"><figcaption>{caption}</figcaption></figure>'
 for page,anchor,file,es,eng in [
 ('profesores','<section id="equipo">','sede-academica.jpg','Sede académica del OAN · Ciudad Universitaria, Bogotá.','OAN campus observatory · Ciudad Universitaria, Bogotá.'),
 ('egresados','<section id="comunidad">','sede-academica.jpg','Un lugar de encuentro para la comunidad del Observatorio.','A meeting place for the Observatory community.'),
 ('amigos','<section id="idea">','sede-historica.png','Sede histórica del Observatorio Astronómico Nacional.','Historic National Astronomical Observatory.'),
 ]:
  p=root/(page+'.html');s=p.read_text();caption=eng if en else es
  if 'class="editorial-image"' not in s:s=s.replace(anchor,anchor+image(file,caption,caption),1)
  p.write_text(s)
 # Identity for the AI and conference imagery in the homepage cards.
 p=root/'index.html';s=p.read_text()
 for heading,file,alt in [('isleIA','isleia-identidad.png','isleIA · la IA del OAN'),('Thursdays under the Stars' if en else 'Jueves bajo las estrellas','talks/Syagimzi1Xw.jpg','Jueves bajo las estrellas · isleIA')]:
  target='<h3>'+heading+'</h3>'
  if f'src="{prefix}{file}"' not in s:
   s=s.replace(target,f'<img class="card-visual'+(' identity' if heading=='isleIA' else '')+f'" src="{prefix}{file}" alt="{alt}" loading="lazy">'+target,1)
 p.write_text(s)

for en in (False,True):
 root=D/'en' if en else D;prefix='../assets/' if en else 'assets/'
 p=root/'index.html';s=p.read_text()
 if 'class="cosmos-collage"' not in s:
  tiles=[('solar.jpg','Our star · SDO' if en else 'Nuestra estrella · SDO'),('pillars.jpg','Pillars of Creation · Webb' if en else 'Pilares de la Creación · Webb'),('rho-ophiuchi.jpg','Rho Ophiuchi · Webb'),('deep-field.jpg','Deep field · Webb' if en else 'Campo profundo · Webb')]
  collage='<div class="cosmos-collage">'+''.join(f'<figure><img src="{prefix}{f}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f,c in tiles)+'</div>'
  s=re.sub(r'(<section class="solar-feature">)<img[^>]+>',lambda m:m[1]+collage,s,count=1)
  s=re.sub(r'<small>(?:Imagen NASA/SDO|NASA/SDO image).*?</small>','<p class="visual-credit">NASA/SDO · NASA, ESA, CSA, STScI. <a href="fuentes.html#imagenes">'+('Image credits' if en else 'Créditos de imágenes')+' ↗</a></p>',s,count=1)
 h='<h3>'+('Cúmulo student group' if en else 'Semillero Cúmulo')+'</h3>'
 if 'cumulo-logo.png' not in s:s=s.replace(h,f'<img class="card-visual identity" src="{prefix}cumulo-logo.png" alt="Logo Cúmulo" loading="lazy">'+h)
 p.write_text(s)
 p=root/'divulgacion.html';s=p.read_text()
 if 'cumulo-logo.png' not in s:
  s=s.replace('<section id="cumulo">','<section id="cumulo"><figure class="cumulo-visual"><img src="'+prefix+'cumulo-logo.png" alt="Logo Cúmulo" loading="lazy"></figure>',1)
 p.write_text(s)
 # Related research imagery complements each group instead of a solitary Sun.
 p=root/'investigacion.html';s=p.read_text()
 titles=[] if 'pillars.jpg' in s else re.findall(r'<article class="card"><h3>(.*?)</h3>',s)
 for title,file in zip(titles[:4],['pillars.jpg','deep-field.jpg','rho-ophiuchi.jpg','sede-historica.png']):
  target='<article class="card"><h3>'+title+'</h3>'
  s=s.replace(target,'<article class="card"><img class="card-visual" src="'+prefix+file+'" alt="'+({'pillars.jpg':'Pillars of Creation · Webb','deep-field.jpg':'SMACS 0723 · Webb','rho-ophiuchi.jpg':'Rho Ophiuchi · Webb','sede-historica.png':'OAN · Bogotá'}[file])+'" loading="lazy"><h3>'+title+'</h3>')
 p.write_text(s)
 # A deep-field photograph introduces the scale of astronomical study.
 p=root/'academia.html';s=p.read_text()
 if 'deep-field.jpg' not in s:
  caption='Galaxies in Webb’s first deep field · NASA, ESA, CSA, STScI.' if en else 'Galaxias en el primer campo profundo de Webb · NASA, ESA, CSA, STScI.'
  s=s.replace('<section id="programas">','<section id="programas"><figure class="editorial-image"><img src="'+prefix+'deep-field.jpg" alt="SMACS 0723 · Webb" loading="lazy"><figcaption>'+caption+'</figcaption></figure>',1)
 p.write_text(s)

for en in (False,True):
 root=D/'en' if en else D;prefix='../assets/' if en else 'assets/'
 p=root/'investigacion.html';s=p.read_text().replace('rho-ophiuchi.jpg','galaxy-m74.jpg').replace('alt="Rho Ophiuchi · Webb"','alt="M74 · Hubble"')
 if 'fuentes.html#imagenes' not in s:s=s.replace('<section id="gosa">','<p class="source-note"><a href="fuentes.html#imagenes">'+('Images: NASA, ESA, CSA, STScI · Full credits' if en else 'Imágenes: NASA, ESA, CSA, STScI · Créditos completos')+' ↗</a></p><section id="gosa">')
 p.write_text(s)
 p=root/'espectra.html';s=p.read_text()
 if 'espectra-cover.jpg' not in s:
  caption='From the archive: eSPECTRA cover, Vol. 3, No. 1 (2025).' if en else 'Del archivo: portada de eSPECTRA, vol. 3, núm. 1 (2025).'
  s=s.replace('<section id="revista">','<section id="revista"><figure class="editorial-image magazine-cover"><img src="'+prefix+'espectra-cover.jpg" alt="eSPECTRA · 2025" loading="lazy"><figcaption>'+caption+'</figcaption></figure>')
 p.write_text(s)
 p=root/'index.html';s=p.read_text();h='<h3>'+('eSPECTRA magazine' if en else 'Revista eSPECTRA')+'</h3>'
 if 'espectra-cover.jpg' not in s:s=s.replace(h,f'<img class="card-visual identity" src="{prefix}espectra-cover.jpg" alt="eSPECTRA · 2025" loading="lazy">'+h)
 p.write_text(s)

from html import escape
credits=json.loads((D.parent/'source/image-credits.json').read_text())
for en in (False,True):
 p=(D/'en' if en else D)/'fuentes.html';s=p.read_text()
 if 'id="imagenes"' not in s:
  items=''.join('<article class="card"><h3>'+escape(c['title'])+'</h3><p>'+escape(c['credit'])+'</p><a href="'+escape(c['source'])+'" target="_blank" rel="noopener">'+('Original image and source' if en else 'Imagen original y fuente')+' ↗</a></article>' for c in credits)
  s=s.replace('</main>','<section class="section" id="imagenes"><h2>'+('Images and visual identity' if en else 'Imágenes e identidad visual')+'</h2><p>'+('Astronomical images are contextual illustrations, not observations made by the OAN. Images have been resized and may be cropped to fit the layout.' if en else 'Las imágenes astronómicas acompañan los temas de investigación; no son observaciones realizadas por el OAN. Se han reducido de tamaño y pueden aparecer recortadas para adaptarse al diseño.')+'</p><div class="two-col">'+items+'</div></section></main>')
 p.write_text(s)
