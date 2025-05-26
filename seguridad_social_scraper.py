import requests
from bs4 import BeautifulSoup

def scrape_seguridad_social():
    url = "https://subastas.seg-social.gob.es/subastas.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    resultados = []

    tabla = soup.find("table", {"id": "ctl00_ContentPlaceHolder1_gridSubastas"})
    if not tabla:
        return resultados

    filas = tabla.find_all("tr")[1:]  # saltar encabezado

    for fila in filas:
        celdas = fila.find_all("td")
        if len(celdas) < 5:
            continue

        titulo = celdas[0].get_text(strip=True)
        tipo = celdas[1].get_text(strip=True)
        fecha = celdas[2].get_text(strip=True)
        provincia = celdas[3].get_text(strip=True)
        enlace = "https://subastas.seg-social.gob.es/" + celdas[0].find("a")["href"]

        resultados.append({
            "titulo": f"{titulo} ({tipo})",
            "descripcion": f"Ubicación: {provincia}, Fecha: {fecha}",
            "url": enlace
        })

    return resultados
