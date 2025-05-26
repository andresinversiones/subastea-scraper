import feedparser

def scrape_boe_rss():
    url = "https://www.boe.es/rss/subastas.xml"
    feed = feedparser.parse(url)

    resultados = []

    for entry in feed.entries:
        resultados.append({
            "titulo": entry.title,
            "descripcion": entry.description,
            "url": entry.link
        })

    return resultados
