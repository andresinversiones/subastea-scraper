import os
import openai

# Inicializar el cliente de OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analizar_subasta(subasta):
    prompt = f"""
    Analiza esta subasta y di si parece rentable, arriesgada o poco interesante:
    
    Título: {subasta['titulo']}
    Descripción: {subasta['descripcion']}
    URL: {subasta['url']}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un experto en inversión inmobiliaria."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
