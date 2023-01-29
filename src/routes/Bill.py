from flask import Blueprint, request, jsonify

# Database
from database.db import db
# Models 
from models.BillModel import BillModel
from models.BillModel import BillSchema

bill_schema = BillSchema()
bills_schema = BillSchema(many=True)

bill = Blueprint('bill', __name__)


@bill.route('/')
def get_bills():
  try:
    bills = BillModel.query.all()
    result = bills_schema.dump(bills)

    return jsonify(result)

  except Exception as ex:
    return jsonify({'message': str(ex)})


@bill.route('/', methods=['POST'])
def add_bill():
  try:
    date_bill = request.json['date_bill']
    user_id = request.json['user_id']
    value = request.json['value']
    type = request.json['type']
    observation = request.json['observation']

    bill = BillModel(date_bill, user_id, value, type, observation)

    db.session.add(bill)
    db.session.commit()

    return bill_schema.jsonify(bill)

  except Exception as ex:
    return jsonify({'message': str(ex)})


@bill.route('/<id>', methods=['DELETE'])
def delete_bill(id):
  try:
    bill = BillModel.query.get(id)
    if bill != None:
      db.session.delete(bill)
      db.session.commit()
      
      return bill_schema.jsonify(bill)

    return jsonify({'message': 'Bill not deleted.'})
  except Exception as ex:
    return jsonify({'message': str(ex)})

  
@bill.route('/<id>', methods=['PUT'])
def update_bill(id):
  try:
    bill = BillModel.query.get(id)
    if bill != None:
      bill.date_bill = request.json['date_bill']
      bill.user_id = request.json['user_id']
      bill.value = request.json['value']
      bill.type = request.json['type']
      bill.observation = request.json['observation']

      db.session.commit()

      return bill_schema.jsonify(bill)
      
    return jsonify({'message': 'Bill not updated.'})
      
  except Exception as ex:
    return jsonify({'message': str(ex)})