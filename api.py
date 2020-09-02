#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import Flask
from flask_restful import Api, Resource

# Resources
from resources.computersRoute import Computers
from resources.incidentsRoute import Incidents
from resources.problemsRoute import Problems
from resources.scriptsRoute import Scripts
from resources.solutionsRoute import Solutions


app = Flask(__name__)
api = Api(app)


api.add_resource(Computers, '/computers')
api.add_resource(Incidents, '/incidents')
api.add_resource(Problems, '/problems')
api.add_resource(Scripts, '/scripts')
api.add_resource(Solutions, '/solutions')


if __name__ == '__main__':
    app.run(debug=True)