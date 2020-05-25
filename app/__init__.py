from flask import Flask
import os


app = Flask(__name__, static_folder="static")
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from app import routes
