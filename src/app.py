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
from models import db, User,People,Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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

@app.route('/user', methods=['GET'])
def handle_hello():
    all_user=User.query.all()
    all_user=list(map(lambda x: x.serialize(),all_user))
    return jsonify(all_user),200
    
@app.route('/people', methods=['GET','POST'])
def get_all_people():
    if request.method == 'GET':
        all_people=People.query.all()
        all_people=list(map(lambda x: x.serialize(),all_people))
        return jsonify(all_people),200

    if request.method == 'POST':
        body= request.get_json()
        character= People(
            name=body['name'],
            height=body['height'],
            mass=body['mass'],
            hair_color=body['hair_color'],
            skin_color =body['skin_color'],
            birth_year=body['birth_year'],
            homeworld=body['homeworld'],
            url=body['homeworld'],
        )
        db.session.add(character)
        db.session.commit()
        response_body={
        "msg": "Character added correctly¿"
        }
        return jsonify(response_body), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_single_person(people_id):
    if request.method == 'GET':
        poeple1=People.query.get(people_id)
        return jsonify(people1.serialize()), 200
    return "Invalid Method", 404

@app.route('/planets', methods=['GET'])
def get_all_planets():
    if request.method == 'GET':
        all_planets=Planets.query.all()
        all_planets=list(map(lambda x: x.serialize(),all_planets))
        return jsonify(all_planets),200

@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_single_planet(planets_id):
    if request.method == 'GET':
        planets1 = Planets.query.get(planets_id)
        return jsonify(planets1.serialize()), 200
    return "Invalid Method", 404

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_person(people_id):
    person1=User.query.get(peope_id)
    if person1 is None:
        raise APIException("User not found",status_code=404)
    db.session.delete_person(people_id)
    db.session.commit()
    return jsonify(), 200
    return "Invalid Method", 404
   
    
    
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
