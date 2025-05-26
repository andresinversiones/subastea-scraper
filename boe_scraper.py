import requests
from bs4 import BeautifulSoup

def scrape_boe():
    url = "https://subastas.boe.es/subastas_ava.php?campo%5B%5D=BIEN&dato%5B%5D=INMUEBLE"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    resultados = []

    filas = soup.select("table tr")[1:]  # Saltamos encabezado

    for fila in filas:
        columnas = fila.find_all("td")
        if len(columnas) < 4:
            continue

        enlace_relativo = columnas[0].find("a")["href"]
        enlace = "https://subastas.boe.es/" + enlace_relativo
        titulo = columnas[0].get_text(strip=True)
        lugar = columnas[1].get_text(strip=True)
        tipo_bien = columnas[2].get_text(strip=True)
        fecha = columnas[3].get_text(strip=True)

        resultados.append({
            "titulo": f"{titulo} ({tipo_bien})",
            "descripcion": f"Ubicación: {lugar}, Fecha: {fecha}",
            "url": enlace
        })

    return resultados
