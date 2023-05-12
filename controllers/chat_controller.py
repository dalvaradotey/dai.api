from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from providers.firebase import firebase_db, firestore

chat_bp = Blueprint('chat', __name__)

collection_ref = firebase_db.collection('chats')

@chat_bp.route('/chats', methods=['GET'])
@cross_origin()
def findAll():
  data = collection_ref.stream()
  listData = []

  for el in data:
    item = el.to_dict()
    item.update({ 'id': el.id })
    listData.append(item)

  return jsonify(listData)

@chat_bp.route('/chats/<string:id>', methods=['GET'])
@cross_origin()
def findOne(id):
  data = collection_ref.document(id).get().to_dict()

  if data:
    data.update({ 'id': id })

  return jsonify(data)

@chat_bp.route('/chats', methods=['POST'])
@cross_origin()
def add():
  payload = request.json
  
  newData = collection_ref.add(payload)
  createdData = collection_ref.document(newData[1].id).get().to_dict()
  createdData.update({ 'id': newData[1].id })

  return jsonify(createdData)

@chat_bp.route('/chats/<string:id>', methods=['PUT'])
@cross_origin()
def update(id):
  payload = request.json
  
  if (payload.get('messages')):
    payload = {
      'messages': firestore.ArrayUnion(payload.get('messages'))
    }
  
  collection_ref.document(id).set(payload, merge=True)
  updatedData = collection_ref.document(id).get().to_dict()
  updatedData.update({ 'id': id })

  return jsonify(updatedData)