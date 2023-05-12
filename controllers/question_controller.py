from flask import Blueprint, request
from flask_cors import cross_origin
import providers.gpt as gpt

question_bp = Blueprint('question', __name__)

@question_bp.route('/questions', methods=['POST'])
@cross_origin()
def make_question():
  payload = request.json
  text = gpt.get_response(payload.get("text"), payload.get("chatUserName"))

  return { 'text': text }