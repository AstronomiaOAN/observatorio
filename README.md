# Observatorio Astronómico Nacional de Colombia

Portal web en español. Versión preparada el 19 de septiembre de 2026, con investigación documental realizada el 16 de septiembre.

## Abrir el sitio

Descomprime el ZIP y abre **dist/index.html** en Chrome, Safari, Firefox o Edge. No necesita instalar dependencias ni ejecutar un servidor. Mantén juntas las páginas HTML y la carpeta assets.

La navegación, el buscador y los filtros de la mediateca funcionan localmente. Los artículos, videos, portales de servicios y otros enlaces externos necesitan internet. Los enlaces de correo abren la aplicación de correo del visitante; no envían mensajes automáticamente.

## Contenido

- Inicio y presentación de las sedes.
- Academia: posgrados, admisiones y recursos.
- Directorio de diez profesores y contactos institucionales.
- Cuatro grupos del directorio oficial, GoSA y recursos de colaboración.
- Laboratorios: cúpula grande, cúpula pequeña y fotografía/cuarto oscuro.
- Historia, cronología, patrimonio instrumental, jardín y fuentes de archivo.
- Divulgación, Cúmulo y canales de comunicación.
- Revista eSPECTRA y enlaces de lectura.
- Mediateca con 22 registros, búsqueda y filtros por formato.
- Visitas, Domo Planetario y asesorías.
- Egresados y Amigos del Observatorio.
- Fuentes, créditos y catálogo de enlaces.

## Editar y publicar

Las páginas de **dist/** son HTML editables. El diseño se controla desde **dist/assets/styles.css**; el menú y los filtros, desde **dist/assets/app.js**. No se usan frameworks, CDNs, bibliotecas remotas ni analítica.

Para publicar en un servidor estático, sube el contenido de **dist/** a la carpeta pública del alojamiento. El index.html debe quedar en su raíz. Los nombres de archivo y las rutas son relativos.

Los CSV **fuentes.csv** y **mediateca.csv** permiten reutilizar las referencias. En **source/** se incluyen los scripts Python de generación editorial y sus datos. Los HTML de dist son la versión final canónica: los scripts son auxiliares, y ejecutarlos vuelve a generar algunas páginas; pueden sobrescribir cambios realizados directamente en HTML.

## Alcance editorial

La mediateca es una selección documentada, no un inventario exhaustivo. Los contenidos externos permanecen en sus plataformas originales; no se incluyen copias de artículos completos, videos o archivos históricos.

Amigos del Observatorio es una propuesta por definir institucionalmente. No se han creado membresías, pagos ni inscripciones. Egresados incluye recursos institucionales sin publicar datos personales no autorizados.

Consultar **dist/fuentes.html** para procedencia y créditos de fotografías. Antes de sustituir el portal oficial, revisar contenidos, datos operativos, identidad institucional y permisos de las imágenes. La fotografía histórica y la del campus no tienen una licencia abierta explícita en las fuentes consultadas.

## Verificación

Se comprobó la sintaxis JavaScript, la existencia de las páginas y los recursos locales, los destinos internos y las anclas. Las imágenes fueron inspeccionadas. El diseño incluye reglas adaptables para móvil y escritorio, navegación por teclado y respeto a la preferencia de movimiento reducido. No se realizó una prueba visual en navegador.

## Actualización bilingüe — 24 de septiembre de 2026

- 15 páginas en español y sus 15 equivalentes en `dist/en/`.
- Selector ES / EN en todas las páginas; mantiene la página y el ancla actual.
- `jueves.html`: 19 conferencias del canal oficial con miniaturas locales, búsqueda por texto, filtros 2025/2026 y enlace directo a cada grabación. Es una selección, no todo el histórico del canal.
- `isleia.html`: información documentada, grabación de lanzamiento y contacto. No se ha confirmado una URL pública del agente; no se simula un chatbot.
- Fechas del catálogo: publicación en YouTube, no necesariamente fecha de realización. Lanzamiento de IsleIA: 7 de mayo de 2026, documentado en el anuncio de Santiago Vargas.
- Los textos del portal están traducidos; nombres propios, fuentes originales, videos y carteles conservan su idioma. Traducciones editoriales no oficiales.
- Navegación y búsqueda funcionan al abrir `dist/index.html` directamente. Videos y enlaces externos requieren internet.

### Archivos y edición

El HTML de `dist/` es la versión publicable. Los scripts históricos `build_pages.py` y `build_archive.py` anteceden esta actualización y pueden sobrescribir cambios: no ejecutarlos sobre la versión final sin una copia.
`source/extend_portal.py` reproduce las secciones nuevas y la traducción a partir del HTML español, las traducciones y el snapshot de YouTube. Conserva el contenido existente. `source/en-translations.txt` y `translations-en.json` contienen la traducción editorial. Los identificadores, fuentes y títulos de las conferencias están en `source/conferencias.json`; los datos extraídos originalmente están en `source/youtube-extracted.json`.

### Extraer nuevos metadatos de YouTube

Se incluye `source/import_youtube.py`, que consulta la API oficial YouTube Data API v3. Requiere Python 3 y una clave propia con esa API activada, guardada únicamente en la variable de entorno `YOUTUBE_API_KEY`. No se incluye ni se requiere una clave para navegar por la web entregada.

```bash
python source/import_youtube.py --output youtube-candidates-2026.json --max-pages 20
```

Exporta título, descripción, miniatura, URL, fecha de publicación, inicio de transmisión cuando existe y duración. Recorre páginas de 50 videos y avisa si el límite impide recuperar todo. No publica automáticamente: revisar cuáles pertenecen al ciclo, traducir los títulos y añadir los seleccionados al catálogo. La API puede consumir cuota del proyecto del titular. El importador se ha revisado y comprobado sintácticamente; no se ejecutó contra la API porque no se proporcionó una clave. Documentación: https://developers.google.com/youtube/v3/docs/playlistItems/list y https://developers.google.com/youtube/v3/docs/videos/list.

### Créditos añadidos

Miniaturas: canal Observatorio Astronómico Nacional de Colombia, https://www.youtube.com/@astronomiaoan. Cada ficha enlaza a su video original. Los derechos de las imágenes pertenecen a sus titulares; confirmar la autorización para una publicación institucional. Las miniaturas se incluyen localmente para que la biblioteca no dependa de un servidor externo de imágenes.
Fuentes de IsleIA: anuncio de Santiago Vargas del lanzamiento del 7 de mayo de 2026; video `Syagimzi1Xw` del canal OAN; UNAL Periódico (19 de abril de 2026); pieza de Televisión UNAL `jD9NjuPwP3A`. La fecha de consulta de estas adiciones es el 24 de septiembre de 2026.

## English quick start

Open `dist/en/index.html`, or use EN on any Spanish page. All 15 portal pages have English counterparts. The downloadable CSV and JSON catalogues include both Spanish and English titles. Videos, posters and external sources retain their original language. The static website works without installation; videos and external links require internet. To import new public video metadata, use the Python utility above with your own YouTube Data API key. Imported candidates require editorial review and translation before publication.

Actualización de imágenes: logo del encabezado y fotografías de las dos sedes suministrados por el usuario. Los originales se incluyen sin modificar en dist/assets/logo-oan.png, sede-historica.png y sede-academica.jpg.

Actualización de isleIA: se restaura el nombre del Observatorio junto al logo en el encabezado; se adopta la escritura «isleIA»; la descripción y sus cuatro características se actualizan con el texto suministrado por el responsable del proyecto. Incluye el reproductor embebido de TikTok de Televisión UNAL y un enlace alternativo al informe. Se retiró el enlace al artículo de UNAL Periódico de la página y de la lista visible de fuentes. La reproducción requiere conexión y disponibilidad de TikTok; no fue posible verificarla desde este entorno.

Actualización posterior: se recupera OAN/1803 junto al logo; la identidad gráfica de isleIA utiliza el archivo original adjunto. Diez enlaces CvLAC extraídos del directorio docente oficial (consulta 24 de septiembre de 2026), con correspondencias en source/faculty-cvlac.json. El recorrido de Facebook de Bogotá UNAL sustituye la fotografía inicial de patrimonio e incluye enlace alternativo; su reproducción depende de Facebook y del navegador, y no se pudo verificar desde este entorno.

Recorrido de patrimonio actualizado: video de YouTube 9gAK0wLzbLM, embebido en español e inglés en sustitución de Facebook.

### Reproducción de YouTube / error 153
YouTube requiere el encabezado HTTP Referer del sitio que lo integra. Se configuró explícitamente `strict-origin-when-cross-origin` en la página de patrimonio y en su iframe. Para la copia descargada, ejecutar `python3 iniciar_web.py` y abrir http://127.0.0.1:8000; o consultar la web publicada. Abrir `dist/index.html` con doble clic permite navegar, pero los archivos file:// no envían esa identificación: en ese caso se muestra un acceso a la web y a YouTube en lugar del reproductor que da error. Extensiones o políticas del navegador que supriman Referer todavía pueden impedir la reproducción. No se ha confirmado reproducción de extremo a extremo en el navegador del usuario.
