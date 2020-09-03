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
        raise NotImplementedError

    
    def post(self):
        '''
        Criar problema
        '''
        raise NotImplementedError
    
    
    def patch(self):
        '''
        Ativar/ desativar problema
        '''
        raise NotImplementedError