import os
import psycopg2
from psycopg2.extras import RealDictCursor
from ia import analizar_subasta  # Importa la función desde ia.py

# Obtener la URL de conexión desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL no está definida.")

# Función para conectarse a la base de datos
def conectar_db():
    print("🟡 Conectando a la base de datos...")
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

# Función para guardar una subasta de prueba
def guardar_subasta():
    print("📥 Guardando subasta de ejemplo...")
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS subastas (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            descripcion TEXT,
            url TEXT
        )
    """)
    cur.execute("""
        INSERT INTO subastas (titulo, descripcion, url)
        VALUES (%s, %s, %s);
    """, (
        "Subasta de prueba",
        "Esto es una entrada de prueba para análisis con IA.",
        "https://ejemplo.com"
    ))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Subasta guardada correctamente.")

# Ejecutar
if __name__ == "__main__":
    print("🚀 Ejecutando scraper...")
    guardar_subasta()

    subasta = {
        "titulo": "Subasta de prueba",
        "descripcion": "Esto es una entrada de prueba para análisis con IA.",
        "url": "https://ejemplo.com"
    }

    print("🤖 Analizando subasta con IA...")
    resultado = analizar_subasta(subasta)
    print("🧠 Resultado IA:", resultado)
