from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/secure_file_sharing'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from app import routes
