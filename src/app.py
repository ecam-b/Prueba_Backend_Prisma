from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# config
from config import DATABASE_URI_CONNECTION, SECRET_KEY
# database
from database.db import db
# Routes
from routes import User

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)
Marshmallow(app)

db.init_app(app)
with app.app_context():
  db.create_all()

if __name__ == "__main__":

  # Blueprints
  app.register_blueprint(User.user) # No se establece el url_prefix

  app.run(debug=True)