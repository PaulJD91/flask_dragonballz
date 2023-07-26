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

@app_blueprint.route("/characters", methods=['POST'])
def create_character():
    name = request.form['name']
    race = request.form['race']
    alignment = request.form['alignment']
    special_move = request.form['special_move']
    power_level = request.form['power_level']
    stage_id = request.form['stage_id']

    character = Character(name=name, race=race, alignment=alignment, special_move=special_move, stage_id=stage_id)

    db.session.add(character)
    db.session.commit()
    return redirect('/')

@app_blueprint.route("/stages/<id>")
def show_stage(id):
    stage = Stage.query.get(id)
    return render_template("stages/show.html", stage=stage)

@app_blueprint.route("/characters/<id>")
def show_character(id):
    character = Character.query.get(id)
    return render_template("characters/show.html", character=character)
