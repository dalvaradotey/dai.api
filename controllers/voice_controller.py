from flask import Blueprint, request, send_file
from flask_cors import cross_origin
import providers.eleven as eleven

voice_bp = Blueprint('voice', __name__)

@voice_bp.route('/voices', methods=['POST'])
@cross_origin()
def make_voice():
  payload = request.json
  audio = eleven.make_audio(payload.get("text"))

  return send_file(audio)