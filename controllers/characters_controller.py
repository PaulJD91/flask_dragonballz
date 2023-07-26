from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Character, Stage

characters_blueprint = Blueprint("characters", __name__)

@characters_blueprint.route("/")
def home():
    stages = Stage.query.all()
    return render_template('index.html', stages=stages)

@characters_blueprint.route("/stages/new")
def create_stage():
    return render_template("stages/new.html")

@characters_blueprint.route("/characters/new")
def create_character():
    return render_template("characters/new.html")