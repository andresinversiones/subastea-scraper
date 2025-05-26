import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Obtener la URL de conexión desde las variables de entorno de Railway
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL no está definida.")

# Función para conectarse a la base de datos
def conectar_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

# Función para insertar una subasta de prueba
def guardar_subasta():
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
        "Esto es una subasta de ejemplo generada automáticamente.",
        "https://ejemplo.com/subasta"
    ))
    conn.commit()
    cur.close()
    conn.close()

# Ejecutar
if __name__ == "__main__":
    print("✅ Ejecutando scraper...")
    guardar_subasta()
    print("✅ Subasta guardada correctamente.")
