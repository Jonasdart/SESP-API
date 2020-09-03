#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource


class Incidents(Resource):
    def get(self):
        '''
        Retornar incidente
        '''
        raise NotImplementedError

    
    def post(self):
        '''
        Criar incidente
        '''
        raise NotImplementedError
    
    
    def patch(self):
        '''
        Ativar/ desativar incidente
        '''
        raise NotImplementedError