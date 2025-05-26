import os
from openai import OpenAI

def analizar_subasta(subasta):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    prompt = f"""
Eres un experto en inversiones y subastas. Analiza esta subasta y dime si parece una buena oportunidad:

Título: {subasta['titulo']}
Descripción: {subasta['descripcion']}
URL: {subasta['url']}

Responde con un resumen profesional en una línea.
"""

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Eres un asesor de inversiones experto en subastas."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
     
