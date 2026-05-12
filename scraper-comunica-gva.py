import os
import json
import requests
from bs4 import BeautifulSoup
import markdownify
from langdetect import detect, LangDetectException

def scrap_noticia_en_idioma(bs, y, base_filename, consellerias, url, idx):
    title_html = subtitle_html = content_html = ""
    title = bs.find('h2', {'class': 'custom-title-page'})
    if title:
        title_html = str(title)
        title = title.text.strip()

    date = bs.find('div', {'class': 'row info'})
    if date:
        date = date.find_all('div', {'class': 'col-lg-12'})
        if date:
            date = date[1]
            date = date.text.strip()

    subtitle = bs.find('div', {'class': 'entradilla col-sm-9'})
    if subtitle:
        subtitle_html = str(subtitle)
        subtitle = subtitle.text.strip()

    content = bs.find('div', {'class': 'cuerpo-noticia'})
    if content:
        content_html = str(content)
        content = content.text.strip()
        try:
            idioma = detect(content)
        except LangDetectException:
            return None

        lang = {1: 'va', 2: 'es'}[y]
        if idioma != lang:
            if idioma == "ca" and lang == "va":
                print("valenciano")
            else:
                return None

        html_filename = os.path.join("Turismo", lang, "consellerias", "html", "2026-01", f"{base_filename}.html")
        md_filename = os.path.join("Turismo", lang, "consellerias", "md", "2026-01", f"{base_filename}.md")
        txt_filename = os.path.join("Turismo", lang, "consellerias", "plain", "2026-01", f"{base_filename}.txt")

        with open(html_filename, "wb") as f:
            f.write(response._content)

        html = title_html + '\n' + subtitle_html + '\n' + content_html
        markdown = markdownify.markdownify(str(html), heading_style="ATX")
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(markdown)

        with open(txt_filename, "w", encoding="utf-8") as f:
            f.write(content)

        consellerias.append({
            'source': url,
            'title': title,
            'subtitle': subtitle,
            'date': date,
            'path2html': f'./html/2026-01/{lang}/{base_filename}.html',
            'path2txt': f'./plain/2026-01/{lang}/{base_filename}.txt',
            'path2md': f'./md/2026-01/{lang}/{base_filename}.md'
        })

        ruta = os.path.join("Turismo", lang, "consellerias", "index.json")
        f = open(os.getcwd() + "\\" + ruta, "w+", encoding='utf-8')
        f.write(json.dumps(consellerias, indent=4, ensure_ascii=False))
        print("NOTICIA: " + url + " DESCARGADA. IDX = " + str(idx))
    else:
        return None

if __name__ == '__main__':
    consellerias_cas = []
    consellerias_val = []
    title = subtitle = ''
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    idx = 0
    response = requests.get(
        f"https://comunica.gva.es/va/totes",
        headers=HEADERS)
    for i in range(1, 710):
        if i > 1:
            response = requests.get(f"https://comunica.gva.es/va/totes?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_PPjIHQnjlhdQ&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_PPjIHQnjlhdQ_delta=20&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_PPjIHQnjlhdQ_cur={i}",
                                    headers=HEADERS)
        if response.status_code == 200:
            data = response.text
            bs_p = BeautifulSoup(data, "html.parser")
            if bs_p:
                noticias = bs_p.find('div', {'class': 'news cards cards-md-vertical row'}).find_all('div', {'class': 'cards-container'})
                for noticia in noticias:
                    idx += 1
                    url = noticia.find('a').get('href')
                    # if href.startswith('http'):
                    #     url = href
                    # else:
                    #     url = "https://www.uv.es" + href
                    response = requests.get(url, headers=HEADERS)
                    if response.status_code == 200:
                        data = response.text
                        bs = BeautifulSoup(data, "html.parser")
                        if bs:
                            castellano = bs.find('div', {'class': 'language dropdown-item p-0'})
                            base_filename = "noticia" + str(idx)
                            for y in range(1, 3):
                                if y == 1:
                                    resultado = scrap_noticia_en_idioma(bs, y, base_filename, consellerias_val, url, idx)
                                if y == 2:
                                    url = "https://comunica.gva.es" + castellano.find('a').get('href')
                                    response = requests.get(url, headers=HEADERS)
                                    if response.status_code == 200:
                                        data = response.text
                                        url = response.url
                                        bs = BeautifulSoup(data, "html.parser")
                                        if bs:
                                            resultado = scrap_noticia_en_idioma(bs, y, base_filename, consellerias_cas, url, idx)


                            #filename = title.lower().replace(' ', '_').replace('/', '_')
                            #filename = re.sub(r'[\\/*?:"<>|¿\t\n]', '_', filename)
                            #base_filename = f"{filename}"


                            # ❌ Si ya existe el HTML, no seguimos con esta noticia
                            #if os.path.exists(html_filename):
                            #    print(f"NOTICIA YA EXISTE: {html_filename}")
                            #    continue
                print("PÁGINA: " + str(i) + " DESCARGADA.")