#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource


class Solutions(Resource):
    def get(self):
        '''
        Retornar script
        '''
        raise NotImplementedError

    
    def post(self):
        '''
        Criar script
        '''
        raise NotImplementedError
    

    def put(self):
        '''
        Editar script
        '''
        raise NotImplementedError

    
    def patch(self):
        '''
        Ativar/ desativar script
        '''
        raise NotImplementedError