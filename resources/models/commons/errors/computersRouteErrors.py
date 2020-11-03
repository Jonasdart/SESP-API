#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from datetime import datetime
from resources.models.commons.database_manager import Database
from resources.models.commons.mysql_manager import Gera_query

class ErrorController():
    def __init__(self, error, route, method, applicant):
        self.error = str(error)
        self.route = route
        self.method = method
        self.applicant = applicant

        self.log_register()


    def log_register(self):
        try:
            with open('resources/models/commons/errors/log.log', 'a') as log:
                log.write(f'Route: {self.route}\t\tMethod:{self.method}\t\tApplicant:{self.applicant}\t\tError:{self.error}\t\tWhen:{str(datetime.now())}\n')
            
            query = Gera_query().inserir_na_tabela('api_logs', ['type_id', 'route', 'method', 'applicant','body'], ['1', f'"{self.route}"', f'"{self.method}"', f'"{self.applicant}"', self.error])
                        
            Database().commit_without_return(query)
        
        except Exception as e:
            with open('resources/models/commons/errors/log.log', 'a') as log:
                log.write(f'Route: LogRegister\t\t\t\t\tMethod:\t\t\tApplicant:{self.applicant}\t\tError:{e}\t\tWhen:{str(datetime.now())}\n')
            raise e
        
        raise self.error

