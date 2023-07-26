from flask import Flask, render_template, redirect, request, Blueprint
from app import db
from models import Character, Stage

app_blueprint = Blueprint("characters", __name__)

@app_blueprint.route("/")
def home():
    stages = Stage.query.all()
    return render_template('index.html', stages=stages)

@app_blueprint.route("/stages/new")
def add_stage():
    return render_template("stages/new.html")

@app_blueprint.route("/characters/new")
def add_character():
    return render_template("characters/new.html")

@app_blueprint.route("/stages", methods=['POST'])
def create_stage():
    name = request.form['name']
    terrain = request.form['terrain']
    weather = request.form['weather']

    stage = Stage(name=name, terrain=terrain, weather=weather)

    db.session.add(stage)
    db.session.commit()
    return redirect('/')

