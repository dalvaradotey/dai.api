from flask import Flask
from flask_cors import cross_origin
from controllers.question_controller import question_bp
from controllers.chat_controller import chat_bp
from controllers.voice_controller import voice_bp

app = Flask(__name__)

app.register_blueprint(question_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(voice_bp)

@app.route('/')
@cross_origin()
def index():
  return 'Server Works Fine!'
