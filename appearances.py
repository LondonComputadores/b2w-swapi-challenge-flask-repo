from flask import Flask, request
from flask_restful import Resource
import requests
import json
import swapi

class SWAPI:
    def planets_appearances(self, planet):
        resp = requests.get(f'https://swapi.dev/api/about/') #or .../api/planets
        return json.loads(resp.content)

class Appears(Resource):
    def get_filmes(self, planet):
        """
        Returns the number of times a planet appeared in a movie
        """
        if not isinstance(planet, str):
            raise TypeError("planet argument must be str.")
        planet = self.find_planet(planet)
        if planet:
            return len(planet['films'])
        return 0 