from flask import Blueprint, request, jsonify

# Database
from database.db import db
# Models
from models.UserModel import UserModel
from models.UserModel import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

user = Blueprint('user', __name__)


@user.route('/')
def get_users():
  try:
    users = UserModel.query.all()
    result = users_schema.dump(users)

    return jsonify(result)

  except Exception as ex: 
    return jsonify({'message': str(ex)})   


@user.route("/login", methods=["POST"])
def signup():
  try:
    name = request.json["name"]
    passw = request.json['passw']
    email = request.json["email"]

    user = UserModel(name, passw, email)

    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)
  except Exception as ex:
    return jsonify({"message": str(ex)})