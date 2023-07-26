from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from dotenv import load_dotenv


load_dotenv()
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{PASSWORD}@localhost:5432/dragonballz_app"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Character, Stage

@app.route("/")
def home():
	return "This is the home page!"