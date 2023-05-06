import os
import openai

CHAT_GPT_MODEL = "gpt-3.5-turbo"
CHAT_GPT_SYSTEM = "You are a helpful assistant on a conversation. Answer should be not too long. Be ironic and acid"

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_response(prompt):
  response = openai.ChatCompletion.create(
      model=CHAT_GPT_MODEL,
      messages=[
          {"role": "system", "content": CHAT_GPT_SYSTEM},
          {"role": "user", "content": prompt}
      ]
  )
  return response.choices[0].message.content