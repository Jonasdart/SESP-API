#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

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

@app.route('/')
def home():
    return """
        <!DOCTYPE html>
        <header>
            <meta http-equiv="refresh" content=1;url="http://192.168.0.69/computers/byinventory?inventorynumber=">
        </header>
    """

api.add_resource(Computers.ByInventoryNumber, '/computers/byinventory')
api.add_resource(Computers.ByName, '/computers/byname')
api.add_resource(Computers.ByIpAddress, '/computers/byip')


api.add_resource(Incidents, '/incidents')
api.add_resource(Problems, '/problems')
api.add_resource(Scripts, '/scripts')
api.add_resource(Solutions, '/solutions')


if __name__ == '__main__':
    app.run(host='192.168.0.69', port=80, debug=True)