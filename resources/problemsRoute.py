#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource


class Problems(Resource):
    def get(self):
        '''
        Retornar problema
        '''
        data = request.args
        response = None
        return response

    
    def post(self):
        '''
        Criar problema
        '''
        data = request.get_json()
        response = None
        return response
    
    
    def patch(self):
        '''
        Ativar/ desativar problema
        '''
        data = request.args
        response = None
        return response