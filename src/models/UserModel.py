from database.db import db
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserModel(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  username = db.Column(db.String(50))
  passw = db.Column(db.String(500))
  email = db.Column(db.String(100))
  bills = db.relationship("BillModel")

  def __init__(self, username, passw, email):
    self.username = username
    self.passw = passw
    self.email = email


class UserSchema(ma.Schema):
  class Meta:
    fields = ("id", "username", "passw", "email")