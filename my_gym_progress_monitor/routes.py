from flask import render_template, redirect, url_for, request
from my_gym_progress_monitor import app

@app.route('/', methods = ['GET'])
def index():
    return '<h1>This is main page</h1>'

@app.route('/register', methods = ['GET', 'POST'])
def registration():
    return '<h2>This is registration page</h2>'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return '<h2>This is login page</h2>'

@app.route('/logout', methods = ['GET'])
def logout():
    return '<h2>This is logout page</h2>'

@app.route('/training/new', methods = ['GET', 'POST'])
def new_training():
    return '<h2>This is NEW TRAINING page</h2>'

@app.route('/training/<int:training_id>', methods = ['GET'])
def show_traninig(training_id):
    return f'<h2>This is page for showing information about training with id {training_id}</h2>'

@app.route('/training/<int:training_id>', methods = ['PUT'])
def update_traninig(training_id):
    return f'<h2>This is page for updating information about training with id {training_id}</h2>'

@app.route('/training/<int:training_id>', methods = ['DELETE'])
def delete_traninig(training_id):
    return f'<h2>This is page for training with id {training_id}</h2>'

@app.route('/training/<int:traning_id>/exercise/new', methods = ['GET', 'POST'])
def add_exercise(traning_id):
    return f'<h2>This is page to adding new exercise to trainingo with id {traning_id}</h2>'

@app.route('/training/<int:traning_id>/exercise/<int:exercise_id>', methods = ['GET'])
def showing_exercise(traning_id, exercise_id):
    return f'<h2>This is page to showign exercise with id {exercise_id} from training {traning_id}'

@app.route('/training/<int:traning_id>/exercise/<int:exercise_id>', methods = ['PUT'])
def updating_exercise(traning_id, exercise_id):
    return f'<h2>This is page to updating exercise with id {exercise_id} from training {traning_id}'

@app.route('/training/<int:traning_id>/exercise/<int:exercise_id>', methods = ['DELETE'])
def delete_exercise(traning_id, exercise_id):
    return f'<h2>This is page to deleting exercise with id {exercise_id} from training {traning_id}'

@app.route('/exercise/<int:exercise_id>/set/nwe', methods = ['GET', 'POST'])
def add_new_series(exercise_id):
    return f'<h2>This is page to adding series to exercise with id {exercise_id}'

