import os
import openai

CHAT_GPT_MODEL = "gpt-3.5-turbo"

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_response(prompt, name=''):
  CHAT_GPT_SYSTEM = f'''
    Eres un asistente que responde las preguntas.
    Las respuestas no deben ser demasiada largas.
    Se irónico y acido. 
    Si tienes el nombre de la persona que realiza la pregunta,
    puedes incluir el nombre de vez en cuando.
    No incluyas siempre el nombre de la persona que realiza la pregunta.
    
    - Nombre de la persona que realiza la pregunta: {name}
  '''

  response = openai.ChatCompletion.create(
    model=CHAT_GPT_MODEL,
    messages=[
      {"role": "system", "content": CHAT_GPT_SYSTEM},
      {"role": "user", "content": prompt}
    ]
  )
  return response.choices[0].message.content