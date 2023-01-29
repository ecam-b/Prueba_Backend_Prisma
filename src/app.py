from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# config
from config import DATABASE_URI_CONNECTION, SECRET_KEY
# database
from database.db import db

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

db.init_app(app)
with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True)