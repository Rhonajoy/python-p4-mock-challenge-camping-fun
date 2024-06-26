#!/usr/bin/env python3

from models import db, Activity, Camper, Signup
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask import Flask, make_response, jsonify, request
import os
from flask_cors import CORS


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)


@app.route('/')
def home():
    return ''
@app.route('/campers')
def games():

    campers = []
    for camper in Camper.query.all():
        camper_dict = {
            "name": camper.name,
            "age": camper.age,
            
        }
        campers.append(camper_dict)

    response = make_response(
        jsonify(campers),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
