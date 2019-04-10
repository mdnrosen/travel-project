from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABSE_URI'] = 'postgres://localhost:5432/itchyfeet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
