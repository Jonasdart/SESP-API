#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'


from mysql_manager import Gera_query
import MySQLdb as mdb
import configparser

class Glpi():
    def __init__(self):
        self.connected = False
        self.generate_queries = Gera_query()


    def connect(self):
        if not self.connected:
            credencials = self.authenticate()
            address = credencials.get('Address')
            name = credencials.get('Name')
            user = credencials.get('User')
            password = credencials.get('Password')
        
            try:
                self.bank = mdb.connect(address, user, password, name)
            except:
                self.conected = False
                raise
            else:
                self.cursor = self.bank.cursor()
                self.conected = True

        return {
            'Database' : self.bank,
            'Cursor'   : self.cursor
        }
        

    def disconnect(self):
        if self.connected:
            try:
                self.bank.close()
            except:
                raise Exception('Database connection not initialized')
        
        self.conected = False
        return True


    def authenticate(self):
        """
        Utiliza as informações presentes no glpi.cfg para\n
        retorná-las em forma de lista como credenciais
        Retorno -> Lista:\n
        [0] IP banco, [1] Usuario Banco\n
        [2] Senha Usuario, [3] Nome Banco
        """
        config = configparser.ConfigParser()
        config.read('resources\\models\\commons\\conf.cfg')

        address = config.get('glpi_database', 'address')
        name = config.get('glpi_database', 'name')
        user = config.get('glpi_database', 'user')
        password = config.get('glpi_database', 'password')
        if password == "''":
            password = ''

        return {
            'Address' : address,
            'Name' : name,
            'User' : user,
            'Password' : password
        }

    
    def return_columns(self, table):
        query = self.generate_queries.listar_colunas(table)
        columns = self.commit_with_return(query)
        dict_columns = {

        }

        for column in columns:
            dict_columns[column[0]] = [column[x+1] for x in range(len(column[1:]))]

        return dict_columns


    def commit_without_return(self, query):
        self.connect()
        try:
            self.cursor.execute(query)
        except:
            raise
        else:
            self.bank.commit()
            self.disconnect()
            return True


    def commit_with_return(self, query):
        results = None
        self.connect()
        try:
            self.cursor.execute(query)
        except:
            raise
        else:
            results = self.cursor.fetchall()
            self.disconnect()

        return results