#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource


class Computers(Resource):
    def get(self):
        data = request.args
        response = None
        return response

    
    def post(self):
        data = request.get_json()
        response = None
        return response
    

    def put(self):
        data = request.get_json()
        response = None
        return response

    
    def patch(self):
        data = request.args
        response = None
        return response