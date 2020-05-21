#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'


from glpi import Glpi
from database_manager import Database

class Backend():
    def __init__(self):
        self.database = Database()
        self.glpi = Glpi()


    def return_resume_of_computer(self, data):
        try:
            inventory_number = data['InventoryNumber']
            database = data['Database']

            if database == 'SESP':
                raise Exception('Method are not implemented')
            elif database == 'GLPI':
                computers = self.glpi.return_computer(inventory_number)
                if len(computers) <= 0:
                    raise Exception(f'Nenhum computador encontrado na base de dados com a etiqueta {inventory_number}')
                self.r = {
                    'Message' : computers,
                    'Status'  : 200
                }
        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : 'Return_Resume_of_Computer => ' + str(e)
                },
                'Status' : 404
            }

        return self.r