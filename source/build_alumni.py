"""Build the bilingual alumni directory from sanitized academic records only."""
from pathlib import Path
import json,re,html,datetime
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'dist'
data=json.loads((ROOT/'source/alumni.json').read_text())
def h(s):return html.escape(str(s),quote=True)
def link(url,label):return f'<a href="{h(url)}" target="_blank" rel="noopener">{h(label)} ↗</a>'
for en in (False,True):
 t=lambda es,eng:eng if en else es
 asset='../assets/' if en else 'assets/'
 programs={'especializacion':t('Especialización','Specialization'),'maestria':t('Maestría','Master’s'),'doctorado':t('Doctorado','Doctorate')}
 def fmt(d):
  if not d:return t('Sin fecha registrada','Date not recorded')
  dt=datetime.date.fromisoformat(d)
  months=('January February March April May June July August September October November December' if en else 'enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre').split()
  return f'{months[dt.month-1]} {dt.day}, {dt.year}' if en else f'{dt.day} de {months[dt.month-1]} de {dt.year}'
 groups=[]
 for year in sorted({(r['date'] or '9999')[:4] for r in data}):
  rows=[]
  for r in data:
   if (r['date'] or '9999')[:4]!=year:continue
   links=[]
   if r.get('repository'):links.append(link(r['repository'],t('Consultar trabajo','View thesis')))
   if r.get('video'):links.append(link(r['video'],t('Ver sustentación','Watch defense')))
   links += [link(p['url'],p['label']) for p in r['profiles']]
   missing='' if r.get('repository') else f'<p class="alumni-unavailable">{t("Enlace al repositorio no disponible en las fuentes consultadas.","Repository link unavailable in the consulted sources.")}</p>'
   extra=''
   if r['dateType']=='graduation':extra=f'<p class="alumni-unavailable">{t("Fecha de sustentación: no registrada en la fuente.","Defense date: not recorded in the source.")}</p>'
   if r.get('graduationDate'):extra=f'<p>{t("Grado","Graduation")}: {fmt(r["graduationDate"])}</p>'
   sources=''
   if r.get('sources'):sources='<p class="source-note">'+t('Fuentes: ','Sources: ')+' · '.join(link(s['url'],s['label'] if not en else ['Defense announcement','RAC bulletin 1018 · pp. 24–25'][i]) for i,s in enumerate(r['sources']))+'</p>'
   distinction=f'<span class="alumni-honor">{h(r["distinction"])}</span>' if r.get('distinction') else ''
   search=' '.join(str(r.get(k,'')) for k in ('name','title','supervisor'))
   rows.append(f'''<article class="alumni-card" data-program="{r['program']}" data-year="{year}" data-search="{h(search)}"><div class="alumni-date"><span>{t('Sustentación','Defense') if r['dateType']=='defense' else t('Grado','Graduation')}</span><strong>{fmt(r['date'])}</strong></div><div class="alumni-detail"><div class="alumni-card-top"><span class="alumni-program">{programs[r['program']]}</span>{distinction}</div><h3>{h(r['name'])}</h3><p class="alumni-thesis">{h(r['title'])}</p><p class="alumni-supervisor"><strong>{t('Dirección del trabajo','Thesis supervision')}:</strong> {h(r['supervisor'])}</p>{extra}<div class="alumni-links">{''.join(links)}</div>{missing}{sources}</div></article>''')
  groups.append(f'<section class="alumni-year" data-alumni-year="{year}"><h2>{year if year!="9999" else t("Sin fecha registrada","Date not recorded")}</h2><div>{"".join(rows)}</div></section>')
 years=''.join(f'<option value="{y}">{y if y!="9999" else t("Sin fecha","Undated")}</option>' for y in sorted({(r['date'] or '9999')[:4] for r in data}))
 title=t('Una comunidad que sigue explorando','A community that keeps exploring')
 main=f'''<main id="contenido" class="alumni-page"><section class="alumni-hero"><div><p class="eyebrow">OAN / {t('EGRESADOS','ALUMNI')}</p><h1>{title}</h1><p>{t('Personas, preguntas y trabajos que forman parte de nuestra historia académica. Explora las trayectorias de especialización, maestría y doctorado.','People, questions and theses that shape our academic history. Explore our specialization, master’s and doctoral graduates.')}</p><a class="button" href="#directorio">{t('Explorar el directorio','Explore the directory')} ↓</a></div><figure><img src="{asset}sede-academica.jpg" alt="{t('Sede académica del Observatorio Astronómico Nacional','Academic building of the National Astronomical Observatory')}"><figcaption>{t('El Observatorio: punto de partida de nuevas preguntas.','The Observatory: a starting point for new questions.')}</figcaption></figure></section><div class="content"><div class="alumni-stats" aria-label="{t('Registros incluidos','Included records')}"><div><strong>19</strong><span>{programs['especializacion']}</span></div><div><strong>97</strong><span>{programs['maestria']}</span></div><div><strong>1</strong><span>{programs['doctorado']}</span></div></div><section class="alumni-intro"><p class="eyebrow">{t('MEMORIA ACADÉMICA','ACADEMIC RECORD')}</p><h2>{t('Cada trabajo abre un camino','Every thesis opens a new path')}</h2><p>{t('Consulta 117 registros académicos, ordenados del más antiguo al más reciente. María Gracia Batista Rojas es la única egresada del doctorado incluida en este directorio.','Browse 117 academic records, ordered from earliest to latest. María Gracia Batista Rojas is the only doctoral graduate included in this directory.')}</p><p class="note">{t('Las fechas de maestría corresponden a sustentaciones. En especialización, la fuente solo registra fechas de grado: se muestran con esa etiqueta, sin sustituir la fecha de sustentación. Dos registros no tienen fecha de grado y aparecen al final. Los conteos corresponden a los listados suministrados, no a personas únicas entre programas.','Master’s dates refer to thesis defenses. The specialization source only records graduation dates; these are labelled accordingly and are not treated as defense dates. Two records have no graduation date and appear last. Counts refer to the supplied program lists, not unique people across programs.')}</p></section><section id="directorio" class="alumni-directory"><h2>{t('Directorio de egresados','Alumni directory')}</h2><form class="alumni-filters" role="search"><label>{t('Buscar','Search')}<input id="alumni-search" type="search" placeholder="{t('Nombre, título o director…','Name, thesis or supervisor…')}"></label><label>{t('Programa','Program')}<select id="alumni-program"><option value="all">{t('Todos los programas','All programs')}</option>{''.join(f'<option value="{k}">{v}</option>' for k,v in programs.items())}</select></label><label>{t('Año','Year')}<select id="alumni-year"><option value="all">{t('Todos los años','All years')}</option>{years}</select></label><button type="reset">{t('Limpiar','Reset')}</button></form><p id="alumni-count" class="alumni-count" aria-live="polite">117 {t('registros','records')}</p><p id="alumni-empty" hidden>{t('No encontramos registros con esos filtros. Prueba otro nombre, tema o año.','No records match these filters. Try another name, topic or year.')}</p><div class="alumni-results">{''.join(groups)}</div></section><section id="fuentes-egresados"><h2>{t('Sobre este archivo','About this archive')}</h2><p>{t('Base documental: Relación Graduados Maestría Astronomía Junio-2026 y Especialización en Astronomía, suministradas para este portal. Los 75 enlaces de repositorio de maestría proceden del listado original. Los nombres y títulos conservan la información de las fuentes; en especialización, los nombres aparecen con los apellidos primero.','Documentary basis: Relación Graduados Maestría Astronomía Junio-2026 and Especialización en Astronomía, supplied for this portal. The 75 master’s repository links come from the original list. Names and titles preserve the source information; specialization names are listed surname first.')}</p><p>{t('Los títulos se conservan en su idioma original. Los perfiles externos se incluyen solo cuando se identificó una coincidencia académica. No se publican números de identificación ni datos personales de contacto. Actualización: 2 de octubre de 2026.','Thesis titles retain their original language. External profiles are included only where an academic match was identified. Identification numbers and personal contact details are not published. Updated: October 2, 2026.')}</p><a class="button" href="mailto:obsan_fcbog@unal.edu.co?subject=Actualizacion%20directorio%20egresados">{t('Proponer una actualización','Suggest an update')} ↗</a></section></div></main>'''
 path=D/('en/egresados.html' if en else 'egresados.html')
 page=path.read_text();page=re.sub(r'<main\b.*?</main>',lambda _:main,page,flags=re.S)
 resources='<section id="recursos"><h2>'+t('Servicios para egresados','Alumni services')+'</h2><div class="three-col">'+''.join('<article class="card"><h3>'+label+'</h3>'+link(url,t('Consultar','Explore'))+'</article>' for label,url in [(t('Programa de Egresados UNAL','UNAL Alumni Program'),'http://egresados.unal.edu.co'),(t('Egresados de Ciencias','Science alumni'),'https://ciencias.bogota.unal.edu.co/dependencias/egresados'),(t('Educación continua','Continuing education'),'https://ciencias.bogota.unal.edu.co/educacion_continua/cursos_diplomados_eventos/')])+'</div></section>'
 page=page.replace('<section id="fuentes-egresados">',resources+'<section id="fuentes-egresados">')
 page=re.sub(r'<title>.*?</title>',f'<title>{title} · OAN Colombia</title>',page)
 # Preserve the shared site and load the directory assets exactly once.
 page=re.sub(r'<link rel="stylesheet" href="[^"]*alumni.css">','',page)
 page=re.sub(r'<script defer src="[^"]*alumni.js"></script>','',page)
 page=page.replace('</head>',f'<link rel="stylesheet" href="{asset}alumni.css"><script defer src="{asset}alumni.js"></script></head>')
 path.write_text(page)
print('Built bilingual directory: 117 records per language.')
