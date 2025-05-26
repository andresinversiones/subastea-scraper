import os
import psycopg2
from psycopg2.extras import RealDictCursor
from ia import analizar_subasta
from seguridad_social_scraper import scrape_seguridad_social

# Conexión a la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL no está definida.")

def conectar_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

# Guardar subasta en la base de datos
def guardar_subasta(subasta):
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS subastas (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            descripcion TEXT,
            url TEXT,
            analisis TEXT
        )
    """)
    cur.execute("""
        INSERT INTO subastas (titulo, descripcion, url, analisis)
        VALUES (%s, %s, %s, %s);
    """, (
        subasta["titulo"],
        subasta["descripcion"],
        subasta["url"],
        subasta["analisis"]
    ))
    conn.commit()
    cur.close()
    conn.close()

# Ejecutar flujo completo
if __name__ == "__main__":
    print("🚀 Ejecutando scraper Seguridad Social...")

    subastas = scrape_seguridad_social()
    print(f"🔎 Encontradas {len(subastas)} subastas")

    for subasta in subastas[:5]:  # Limitar a 5 para pruebas
        print(f"🤖 Analizando: {subasta['titulo']}")
        analisis = analizar_subasta(subasta)
        subasta["analisis"] = analisis
        guardar_subasta(subasta)
        print(f"🧠 Resultado IA: {analisis}")

    print("✅ Proceso finalizado.")
