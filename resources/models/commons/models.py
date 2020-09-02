#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'


from resources.models.commons.glpi import Glpi
from resources.models.commons.database_manager import Database
from datetime import datetime

class Backend():
    def __init__(self):
        self.database = Database()
        self.glpi = Glpi()


    def return_date_time(self):
        try:
            date = datetime.now().strftime('%d-%m-%Y')
            time = datetime.now().strftime('%H:%M:%S')

            self.r = {
                'Message' : date + ' ' + time,
                'Date'    : date,
                'Time'    : time,
                'Status'  : 200
            }

        except Exception as e:
            self.r = {
                'Message' : {
                    'Error' : 'Return_date_time => ' + str(e)
                },
                'Status' : 404
            }

        return self.r