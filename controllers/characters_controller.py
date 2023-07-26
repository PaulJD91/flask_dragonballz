from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Character, Stage

characters_blueprint = Blueprint("characters", __name__)

@characters_blueprint.route("/")
def home():
    return render_template('index.html')