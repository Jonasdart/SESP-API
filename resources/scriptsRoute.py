#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource


class Scripts(Resource):
    def get(self):
        '''
        Retornar script
        '''
        data = request.args
        response = None
        return response

    
    def post(self):
        '''
        Criar script
        '''
        data = request.get_json()
        response = None
        return response
    

    def put(self):
        '''
        Editar script
        '''
        data = request.get_json()
        response = None
        return response

    
    def patch(self):
        '''
        Ativar/ desativar script
        '''
        data = request.args
        response = None
        return response