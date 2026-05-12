# 📄 Conselleria de Comunicació GVA Scraper
Este repositorio contiene un script en Python para la extracción y procesamiento de noticias oficiales desde el portal de la [Generalitat Valenciana Comunitat Valenciana - GVA Comunicació](https://comunica.gva.es/va/totes).

El scraper descarga noticias en dos idiomas (valenciano y castellano), detecta automáticamente el idioma del contenido y guarda la información en distintos formatos estructurados.

## 📦 Características del scraper

- Scraping de noticias del portal oficial GVA
- Navegación por paginación (hasta ~700 páginas)
- Extracción de noticias individuales
- Soporte multilenguaje:
  - Valenciano (`va`)
  - Castellano (`es`)
- Detección automática de idioma con `langdetect`
- Exportación de contenido en:
  - HTML original
  - Markdown
  - Texto plano
- Generación de índices JSON por idioma
- Separación automática por idioma y estructura de carpetas

## 🧠 Flujo del script
### 1. Scraping de listado

El script recorre páginas del portal:

```
https://comunica.gva.es/va/totes?p=...
```

### 2. Extracción de noticias

Por cada noticia:
- obtiene URL
- descarga HTML
- identifica versión en castellano
- procesa ambas versiones

### 3. Procesamiento por idioma

Se ejecuta la función:

```
scrap_noticia_en_idioma()
```

Esta función:

- detecta idioma real del contenido
- valida coincidencia con el idioma esperado
- extrae:
  - título
  - subtítulo
  - fecha
  - contenido
- guarda archivos

## ⚙️ Tecnologías utilizadas

- `requests`
- `BeautifulSoup4`
- `markdownify`
- `langdetect`
- `os` / `json` / `re`

Instalación de dependencias:
```
pip install requests beautifulsoup4 markdownify langdetect
```

### 🧾 Datos extraídos

Cada noticia incluye:

| Campo    | Descripción          |
| -------- | -------------------- |
| title    | Título de la noticia |
| subtitle | Entradilla           |
| date     | Fecha de publicación |
| source   | URL original         |
| content  | Texto limpio         |

### 📊 Ejemplo de índice JSON

```
{
  "source": "https://comunica.gva.es/...",
  "title": "Noticia ejemplo",
  "subtitle": "Entradilla...",
  "date": "2026-01-10",
  "path2html": "./html/2026-01/es/noticia1.html",
  "path2txt": "./plain/2026-01/es/noticia1.txt",
  "path2md": "./md/2026-01/es/noticia1.md"
}
```

## 💰 Financiación

Este recurso está financiado por el Ministerio para la Transformación Digital y de la Función Pública — Financiado por la UE – NextGenerationEU, en el marco del proyecto Desarrollo de Modelos ALIA.

## 🙏 Agradecimientos

Expresamos nuestro agradecimiento a todas las personas e instituciones que han contribuido al desarrollo de este recurso.

Agradecimientos especiales a:

[Proveedores de datos]

[Proveedores de soporte tecnológico]

Asimismo, reconocemos las contribuciones financieras, científicas y técnicas del Ministerio para la Transformación Digital y de la Función Pública – Financiado por la UE – NextGenerationEU dentro del marco del proyecto Desarrollo de Modelos ALIA.

## 📚 Referencia

Por favor, cita este conjunto de datos usando la siguiente entrada BibTeX:

```
@misc{scraper_alia_comunica_gva_2026,
  author       = {Espinosa Zaragoza, Sergio and Sep{\'u}lveda Torres, Robiert and Mu{\~n}oz Guillena, Rafael and Consuegra-Ayala, Juan Pablo},
  title        = {ALIA_Comunica GVA Scraper}, 
  year         = {2026},
  institution  = {Language and Information Systems Group (GPLSI) and Centro de Inteligencia Digital (CENID), University of Alicante (UA)},
  howpublished = {\url{https://github.com/gplsi/scraper-alia-comunica-gva}}
}
```

## ⚠️ Aviso Legal

Este recurso puede contener sesgos o artefactos no intencionados.
Cualquier tercero que utilice o implemente sistemas basados en este recurso es el único responsable de garantizar un uso conforme, seguro y ético, incluyendo el cumplimiento de las normativas relevantes en materia de IA y protección de datos.
