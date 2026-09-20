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
