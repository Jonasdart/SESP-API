#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from commons.conf import sesp_server

from flask import Flask
from flask_restful import Api, Resource

# Resources
from resources import computersRoute as Computers
from resources.incidentsRoute import Incidents
from resources.problemsRoute import Problems
from resources.scriptsRoute import Scripts
from resources.solutionsRoute import Solutions


app = Flask(__name__)
api = Api(app)


api.add_resource(Computers.ByInventoryNumber, '/computers/byinventory')
api.add_resource(Computers.ByName, '/computers/byname')
api.add_resource(Computers.ByIpAddress, '/computers/byip')


api.add_resource(Incidents, '/incidents')
api.add_resource(Problems, '/problems')
api.add_resource(Scripts, '/scripts')
api.add_resource(Solutions, '/solutions')


if __name__ == '__main__':
    address, port, debug = sesp_server().values()
    if debug == 'False': 
        debug = False
    else:
        debug = True
    app.run(host=address, port=port, debug=debug)
