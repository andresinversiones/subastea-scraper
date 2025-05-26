import requests
from bs4 import BeautifulSoup

def scrape_boe():
    url = "https://subastas.boe.es/subastas_ava.php?campo%5B%5D=BIEN&dato%5B%5D=INMUEBLE"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    resultados = []

    # Buscar contenedores de subasta
    contenedores = soup.select("div.resultado_subasta")

    for contenedor in contenedores:
        enlace_tag = contenedor.select_one("a")
        enlace = "https://subastas.boe.es/" + enlace_tag["href"]
        titulo = enlace_tag.get_text(strip=True)

        descripcion_tag = contenedor.select_one("div.subasta_detalle")
        descripcion = descripcion_tag.get_text(strip=True) if descripcion_tag else "Sin descripción"

        resultados.append({
            "titulo": titulo,
            "descripcion": descripcion,
            "url": enlace
        })

    return resultados
