from flask import Flask, request, send_file
app = Flask(__name__)
import gpt
import eleven

from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
  return 'Server Works Fine!'

@app.route('/questions', methods=['POST'])
@cross_origin()
def make_question():
  payload = request.json
  text = gpt.get_response(payload.get("text"))
  audio = eleven.make_audio(text)

  return send_file(audio)
