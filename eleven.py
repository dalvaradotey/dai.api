import os
import tempfile

ELEVEN_API_KEY = os.getenv('ELEVEN_API_KEY')
ELEVEN_VOICE_ID = os.getenv('ELEVEN_VOICE_ID')

def make_audio(text):
  import requests

  CHUNK_SIZE = 1024
  url = "https://api.elevenlabs.io/v1/text-to-speech/" + ELEVEN_VOICE_ID

  headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": ELEVEN_API_KEY
  }

  data = {
    "text": text,
    "model_id" : "eleven_multilingual_v1",
    "voice_settings": {
      "stability": 0.4,
      "similarity_boost": 1.0
    }
  }

  response = requests.post(url, json=data, headers=headers)

  with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
    f.flush()
    temp_filename = f.name

  return temp_filename