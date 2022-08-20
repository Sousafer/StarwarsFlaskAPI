"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route("/characters", methods=['GET'])
def getCharacters():
    characters = Characters.query.all()
    listCharacters=list(map(lambda obj:obj.serialize(),characters)) 
    response_body={
        "result":listCharacters
    }
    return jsonify(response_body), 200

@app.route("/characters/<int:id>", methods=['GET'])
def oneCharacters(id):
    single=Characters.query.get(id)
    characters=single.serialize()
    response_body={
        "result":characters
    }
    return jsonify(response_body), 200
    

@app.route("/planets", methods=['GET'])
def getPlanets():
    planets = Planets.query.all()
    listPlanets=list(map(lambda obj:obj.serialize(),characters)) 
    response_body={
        "result":listPlanets
    }
    return jsonify(response_body), 200

@app.route("/planets/<int:id>", methods=['GET'])
def onePlanets(id):
    single=Planets.query.get(id)
    planets=single.serialize()
    response_body={
        "result":planets
    }
    return jsonify(response_body), 200

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
