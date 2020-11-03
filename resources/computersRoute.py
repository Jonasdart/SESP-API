#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from flask import request
from flask_restful import Resource
from commons import conf
from commons.errors import BadURLError, BadInventoryNumberError, BadRequestError, GLPINameError, SESPVersionError
from resources.models.computerModel import ComputerModel as Model
from resources.models.commons.errors.computersRouteErrors import ErrorController


class ByInventoryNumber(Resource):
    def __init__(self):
        try:
            self.model = Model()
            self.computer_host = request.environ['REMOTE_ADDR']

            if str(request.headers['Sesp-Version']) == str(conf.current_version()):
                self.computer_status, computer = self.model._update_computer(request.headers, self.computer_host)

        except Exception as e:
            ErrorController(e, '/computers/byinventory', '__init__', self.computer_host)

 
    def get(self):
        '''
        Usada para buscar informações referentes ao computador com o número de inventário informado
        '''
        try:
            if str(request.headers['Sesp-Version']) != str(conf.current_version()):
                response =  {
                    'current_version' : conf.current_version()
                }
            else:
                data = dict(request.args)            
                if len(data) != 1:
                    raise BadURLError

                inventory_number = data['number']
                if not inventory_number:
                    raise BadInventoryNumberError

                response = {
                    'current_version' : conf.current_version(),
                    'glpi' : self.model._search_in_glpi_by_inventory_number(inventory_number),
                    'sesp' : self.model._search_by_inventory_number(inventory_number)
                }

        except Exception as e:
            ErrorController(e, '/computers/byinventory', 'get', self.computer_host)

        return response
    

    def put(self):
        '''
        Use para configurar o computador no GLPI e consequentemente fisicamente.
        '''
        if request.headers['Sesp-Version'] != conf.current_version():
            return {
                'current_version' : conf.current_version()
            }

        body = request.get_json()
        header = request.headers
        
        actions = 0
        try:
            
            if(len(body) != 4):
                raise BadRequestError

            inventory_number = header['inventory_number']
            change_name = body['change_name']
            force_inventory = body['force_inventory']
            schedule_reboot = body['schedule_reboot']
            schedule_shutdown = body['schedule_shutdown']

            if not inventory_number:
                raise BadInventoryNumberError

            if change_name:
                self.model._change_name_in_glpi(str(inventory_number), change_name)
                actions += 1

            if force_inventory:
                if self.computer_status != 1 and self.computer_status != 6:
                    self.model._force_next_inventory(inventory_number, computer_ipaddress=self.computer_host)
                    actions += 1
                else:
                    raise GLPINameError

            if schedule_reboot:
                self.model._schedule_next_reboot(inventory_number, schedule_reboot)
                actions += 1

            if schedule_shutdown:
                self.model._schedule_next_shutdown(inventory_number, schedule_shutdown)
                actions += 1

            response = {
                'message':f'Success! {actions} actions performed!'
            }

        except Exception as e:
            error = f'The System has been performed {actions} actions, but, a exception has occurred. Consult the documentation to know the order of execution of the actions. description:{e}'
            ErrorController(error, '/computers/byinventory', 'put', self.computer_host)

        return response

    
    def patch(self):
        '''
        Usado para alterar o Status do computador.
        '''
        if request.headers['Sesp-Version'] != conf.current_version():
            return {
                'current_version' : conf.current_version()
            }
            
        try:
            data = dict(request.args)
            header = request.headers

            inventory_number = header['Inventory_Number']
            try:
                status = data['status']
            except:
                pass
            else:
                self.model._update_status_of_computer(inventory_number, status)
            try:
                fusion_executed = data['fusion_executed']
            except:
                pass
            else:
                self.model._schedule_next_inventory(inventory_number)
           
            
        except Exception as e:
            ErrorController(e, '/computers/byinventory', 'patch', self.computer_host)

        return True


class ByName(Resource):
    def __init__(self):
        try:
            self.model = Model()
            self.computer_host = request.host
            self.computer_status, computer = self.model._update_computer(request.headers, self.computer_host)

        except Exception as e:
            ErrorController(e, '/computers/byinventory', '__init__', self.computer_host)


    def get(self):
        '''
        Usada para buscar informações referentes ao computador com o nome informado
        '''
        try:

            data = dict(request.args)            
            if len(data) != 1:
                raise BadURLError

            name = data['name']
            if not name:
                raise BadInventoryNumberError
            
            response = self.model._search_in_glpi_by_name(name)

        except Exception as e:
            ErrorController(e, '/computers/byname', 'get', self.computer_host)

        return response


class ByIpAddress(Resource):
    def __init__(self):
        try:
            self.model = Model()
            self.computer_host = request.host
            self.computer_status, computer = self.model._update_computer(request.headers, self.computer_host)

        except Exception as e:
            ErrorController(e, '/computers/byinventory', '__init__', self.computer_host)


    def get(self):
        try:
            data = request.args
            response = self.model._search_in_glpi_by_ip_address(data)
        except Exception as e:
            ErrorController(e, '/computers/byip', 'get', self.computer_host)

        return response