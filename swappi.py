from flask import Flask, request, Response
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from database.db import initialize_db
from database.models import Planets
from appearances import Appears
import json


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost:27017/b2w-swapi-challenge-flask-repo'
}

initialize_db(app)

api = Api(app)

planets = [
    {
     'id': '0',
     'name': 'tatooine',
     'climate' : 'arid',
     'terrain': 'desert'   
    },
    {
     'id': '1',
     'name': 'alderaan',
     'climate' : 'temperate',
     'terrain': 'grasslands, mountains'  
    },
    {
     'id': '2',
     'name': 'yavin iv',
     'climate' : 'temperate, tropical',
     'terrain': 'jungle, rainforests'  
    }
]

class Planets(Resource):
    def get(self, id):
        #List planets by id and if not found return a message error
        try:
            response = planets[id]

        except AttributeError:
            response = {'status': 'error', 'message': 'Not Found!'}
        return response 

    def put(self, name):
        #Alter data of each planet
        planet = Planets.query.filter_by(name=name).filter()
        data = request.json
        if 'name' in data:
            planet.name = data['name']
            planet.save()
            response = {
            'id': planet.id,
            'name': planet.name,
            'climate': planet.climate, 
            'terrain':planet.terrain
            }
            return response

    def delete(self, name):
        #Exclude a planet then return a message to confirm
        planet = Planets.query.filter_by(name=name).filter()
        message = 'Planet {} deleted succesfully'.format(planet.name)
        planet.delete()
        return {'status':'sucess', 'message': message}

class ListPlanets(Resource):
    #List all planets
    def get(self):        
        return planets 

    def post(self):
        #Create a new planet
        data = request.json
        planet = Planets.query.filter_by(name=data['planet']).first()
        planet = Planets(id=data['id'],
                         name=data['name'],
                         climate=data['climate'],
                         terrain=data['terrain'])
        planet.save()
        response = {
        'id': planet.id,
        'name': planet.name,
        'climate': planet.climate, 
        'terrain': planet.terrain
        }
        return response

        # data = request.get_json()
        # planet = Planets(**data).save()
        # id = planet.id
        # return {'id': str(id)}, 200

class PlanetByName(Resource):
    def get(self, name):
        ##List planets by name and if not found return a message error
        self.name = name
        #planets_dict = {planet['name']:planet for planet in planets}      
        try:
            response = {planet['name']: planet for planet in planets}.get(name,
                                                      {'message': 'not found'})

        except AttributeError:
            response = {'status': 'error', 'message': 'Not Found!'}
        return response


api.add_resource(ListPlanets, '/planets/')
api.add_resource(Planets, '/planets/<int:id>/')
api.add_resource(PlanetByName, '/planets/<string:name>/')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')