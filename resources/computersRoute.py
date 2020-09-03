#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource
from resources.models.computerModel import ComputerModel as Model


class ByInventoryNumber(Resource):

    
    def __init__(self):
        self.model = Model()


    def get(self):
        '''
        Usada para buscar informações referentes ao computador com o número de inventário informado
        '''
        try:

            data = dict(request.args)            
            if len(data) != 1:
                raise Exception('Bad URL request. Consult the documentation to know the parameters.')

            inventory_number = data['inventorynumber']
            if not inventory_number:
                raise Exception('Please inform a valid InventoryNumber')
            
            response = self.model._search_in_glpi_by_inventory_number(inventory_number)

        except Exception as e:
            raise e

        return response
    

    def put(self):
        '''
        Use para configurar o computador no GLPI e consequentemente fisicamente.
        '''
        data = request.get_json()
        actions = 0
        try:
            
            if(len(data) != 5):
                raise Exception('Bad Request')

            inventory_number = data['inventory_number']
            change_name = data['change_name']
            force_inventory = data['force_inventory']
            schedule_reboot = data['schedule_reboot']
            schedule_shutdown = data['schedule_shutdown']

            if not inventory_number:
                raise Exception('Please inform a valid InventoryNumber')

            if change_name:
                self.model._change_name_in_glpi(str(inventory_number), change_name)
                actions += 1
            if force_inventory:
                self.model._force_next_inventory(inventory_number)
                actions += 1
            if schedule_reboot:
                self.model._schedule_next_reboot(inventory_number, schedule_reboot)
                actions += 1
            if schedule_shutdown:
                self.model._schedule_next_shutdown(inventory_number, schedule_shutdown)
                actions += 1

            response = {
                'message':f'Success! {actions} actions performed!'
            }

        except:
            raise Exception(f'The System has been performed {actions} actions, but, a exception has occurred. Consult the documentation to know the order of execution of the actions.')


        return response

    
    def patch(self):
        '''
        Usado para alterar o Status do computador no GLPI para Ativo.
        '''
        data = request.args
        response = None
        return response


class ByName(Resource):

    
    def __init__(self):
        self.model = Model()


    def get(self):
        data = request.args
        response = self.model._search_in_glpi_by_name(data)
        return response


class ByIpAddress(Resource):

    
    def __init__(self):
        self.model = Model()


    def get(self):
        data = request.args
        response = self.model._search_in_glpi_by_ip_address(data)
        return response