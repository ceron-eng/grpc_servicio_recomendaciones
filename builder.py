import logging
from groq import Groq

def generate_recommendation(analysis):
    
    client = Groq(api_key="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")

    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "Habla en español latinoamericano"},
                {"role": "user", "content": f"Hola, aquí están los resultados del análisis: {analysis}. ¿Qué recomendaciones tienes?"}
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False
        )

        # Accediendo al contenido del mensaje de la primera opción
        if completion.choices and len(completion.choices) > 0:
            response_content = completion.choices[0].message.content if hasattr(completion.choices[0].message, 'content') else "No response text available"
            return response_content
        else:
            logging.warning("No valid response received from the model.")
            return "No valid recommendations found."

    except Exception as e:
        logging.error(f"An error occurred while generating recommendations: {e}")
        return "Error generating recommendations."
