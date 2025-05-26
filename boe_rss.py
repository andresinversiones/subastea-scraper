import requests
import xml.etree.ElementTree as ET

def scrape_boe_rss():
    url = "https://www.boe.es/rss/subastas.xml"
    response = requests.get(url)
    tree = ET.fromstring(response.content)

    resultados = []

    for item in tree.findall(".//item"):
        titulo = item.find("title").text
        descripcion = item.find("description").text
        link = item.find("link").text

        resultados.append({
            "titulo": titulo.strip(),
            "descripcion": descripcion.strip(),
            "url": link.strip()
        })

    return resultados
