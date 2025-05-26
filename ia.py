import os
import openai

# Cargar clave API desde entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ ERROR: No se encontró la clave OPENAI_API_KEY.")

# Configurar cliente OpenAI
openai.api_key = OPENAI_API_KEY

# Función que llama a GPT-4 para analizar la subasta
def analizar_subasta(subasta):
    prompt = f"""
    Eres un experto en inversión inmobiliaria. Analiza esta subasta y responde en 3 frases:
    1. ¿Es interesante o no? Justifica.
    2. Riesgo estimado (bajo, medio, alto).
    3. Recomendación final.

    Datos de la subasta:
    Título: {subasta['titulo']}
    Descripción: {subasta['descripcion']}
    URL: {subasta['url']}
    """

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
        )
        return respuesta.choices[0].message["content"].strip()
    except Exception as e:
        return f"❌ ERROR IA: {str(e)}"
