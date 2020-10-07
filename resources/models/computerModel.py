#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from commons import conf

from resources.models.commons.mysql_manager import Gera_query
from resources.models.commons.glpi import Glpi
from resources.models.commons.database_manager import Database
from datetime import datetime, timedelta
import requests
import configparser

class ComputerModel():
    
    
    def _search_in_glpi_by_name(self, name):
        try:
            query = f"""
                select 
                    computer.id as computer_id, 
                    computer.name as computer_name, 
                    computer.otherserial as computer_inventorynumber, 
                    computer.comment as computer_comments,
                    computer.locations_id as computer_location, 
                    locations.completename as location_name,
                    addresses.name as computer_ipaddress
                from glpi_computers as computer 
                inner join glpi_locations as locations on locations.id=computer.locations_id
                inner join glpi_ipaddresses as addresses on addresses.mainitems_id=computer.id

                where computer.name='{name}' and addresses.mainitemtype='Computer'
            """
            header = ['computer_id', 'computer_name', 'computer_inventorynumber', 'computer_comments', 'computer_location', 'location_name', 'computer_ipaddress']
            results = Glpi().commit_with_return(query)

            return_results = {}

            if len(results) == 0:
                raise 'Nenhum Resultado Encontrado'
            else:
                c = 0
                for result in results:
                    info_results = {}
                    x = 0
                    for dado in result:
                        info_results[header[x]] = dado
                        x += 1
                    c += 1
                    return_results[c] = info_results
        except Exception as e:
            raise e

        return return_results


    def _search_by_inventory_number(self, inventory_number):
        try:
            header = ['computer_id', 'computer_name', 'status_id', 'next_fusion_inventory', 'next_reboot', 'next_shutdown', 'glpi_id', 'glpi_name']
            query = Gera_query().buscar_dados_da_tabela('computers', where=True, coluna_verificacao='inventory_number', valor_where=inventory_number, returns=header)
            results = Database().commit_with_return(query)

            return_results = {}

            if len(results) == 0:
                raise 'Nenhum Resultado Encontrado'
            else:
                c = 0
                for result in results:
                    info_results = {}
                    x = 0
                    for dado in result:
                        info_results[header[x]] = dado
                        x += 1
                    c += 1
                    return_results[c] = info_results
        except Exception as e:
            raise e

        return return_results


    def _search_in_glpi_by_inventory_number(self, inventory_number):
        try:

            query = f"""
                select 
                    computer.id as computer_id, 
                    computer.name as computer_name, 
                    computer.otherserial as computer_inventorynumber, 
                    computer.comment as computer_comments,
                    computer.locations_id as computer_location, 
                    locations.completename as location_name,
                    addresses.name as computer_ipaddress
                from glpi_computers as computer 
                inner join glpi_locations as locations on locations.id=computer.locations_id
                inner join glpi_ipaddresses as addresses on addresses.mainitems_id=computer.id

                where computer.otherserial='{inventory_number}' and addresses.mainitemtype='Computer'
            """
            header = ['computer_id', 'computer_name', 'computer_inventorynumber', 'computer_comments', 'computer_location', 'location_name', 'computer_ipaddress']
            results = Glpi().commit_with_return(query)

            return_results = {}

            if len(results) == 0:
                raise 'Nenhum Resultado Encontrado'
            else:
                c = 0
                for result in results:
                    info_results = {}
                    x = 0
                    for dado in result:
                        info_results[header[x]] = dado
                        x += 1
                    c += 1
                    return_results[c] = info_results
        except Exception as e:
            raise e

        return return_results


    def _search_in_glpi_by_ip_address(self, ip_address):
        raise NotImplementedError


    def _change_status(self, inventory_number, status):
        raise NotImplementedError


    def _change_status_in_glpi(self, inventory_number, status):
        raise NotImplementedError


    def _change_name_in_glpi(self, inventory_number, name):
        try:
            query = f"UPDATE `glpi_computers` SET `name` = '{name}' WHERE `glpi_computers`.`otherserial` = '{inventory_number}';"
            Glpi().commit_without_return(query)
        except Exception as e:
            raise e

        return True


    def _force_next_inventory(self, inventory_number, now=True, computer_ipaddress=False):
        try:
            computer = self._search_in_glpi_by_inventory_number(str(inventory_number))
            glpi_id = computer[1]['computer_id']

            if now:
                if not computer_ipaddress:
                    for _computer in computer.values():
                        try:
                            ip = _computer['computer_ipaddress'].split('.')
                            if ip[2] == '0' or ip[2] == '1':
                                computer_ipaddress = _computer['computer_ipaddress']
                                break
                        except:
                            pass
                try:
                    request = f'http://{computer_ipaddress}:62354/now'
                    response = requests.get(request)
                except:
                    query = f'UPDATE `computers` SET `status_id` = 3 WHERE `inventory_number`= {inventory_number};'
                    Database().commit_without_return(query)
                else:                
                    fusion_frequency = conf.fusion_inventory()['inventory_frequency']
                    next_fusion_inventory = datetime.now()+timedelta(days=fusion_frequency)
                    next_fusion_inventory = datetime.strftime(next_fusion_inventory, '%Y-%m-%d %H:%M')
                    
                    query = f'UPDATE `computers` SET `next_fusion_inventory` = "{next_fusion_inventory}" WHERE `inventory_number`= {inventory_number};'
                    Database().commit_without_return(query)
                    query = f"insert into computers_logs(`type_id`, `computer_id`, `body`) values (8, {glpi_id}, 'New inventory has completed succesfully')"
                    Database().commit_without_return(query)

        except Exception as e:
            raise e      


    def _schedule_next_reboot(self, inventory_number, now=False):
        raise NotImplementedError


    def _schedule_next_shutdown(self, inventory_number, now=False):
        raise NotImplementedError


    def _new_computer(self, computer_name, inventory_number, last_request_host):
        try:
            query = Gera_query().inserir_na_tabela('computers', ['computer_name', 'inventory_number', 'status_id', 'last_request_host'], [computer_name, inventory_number, 6, last_request_host])
            Database().commit_without_return(query)

            status, computer_info = self._validate_informations(inventory_number, last_request_host)

            glpi_id = computer_info[1]['computer_id']
            glpi_name = computer_info[1]['computer_name']

            query = f'UPDATE `computers` SET `glpi_id` = {glpi_id}, `glpi_name` = "{glpi_name}" WHERE `inventory_number`= {inventory_number};'
            Database().commit_without_return(query)

            computer_info = self._search_by_inventory_number(inventory_number)
            self._force_next_inventory(inventory_number, computer_ipaddress=last_request_host)
        
        except Exception as e:
            raise e

        return status, computer_info

    
    def _update_computer(self, request_header, computer_host):
        try:
            inventory_number = request_header['Inventory_Number']
            computer_name = request_header['Computer_Name']
            last_request_host = computer_host
            
            try:    
                computer = self._search_by_inventory_number(inventory_number)
                query = f'UPDATE `computers` SET `last_request_host` = "{computer_host}" WHERE `inventory_number`= {inventory_number};'
                Database().commit_without_return(query)

                if computer[1]['computer_name'] != computer_name:
                    query = f'UPDATE `computers` SET `computer_name` = "{computer_name}" WHERE `inventory_number`= {inventory_number};'
                    Database().commit_without_return(query)

                status, computer_info = self._validate_informations(inventory_number, computer_host)


                glpi_id = computer_info[1]['computer_id']
                glpi_name = computer_info[1]['computer_name']

                query = f'UPDATE `computers` SET `glpi_id` = {glpi_id}, `glpi_name` = "{glpi_name}" WHERE `inventory_number`= {inventory_number};'
                Database().commit_without_return(query)

                if status != 1 and status != 2 and status != 6:
                    if computer[1]['next_fusion_inventory'] is None:
                        self._force_next_inventory(inventory_number, computer_ipaddress=last_request_host)

            except Exception as e:
                if e is not AssertionError:
                    status, computer = self._new_computer(computer_name, inventory_number, last_request_host)
                else:
                    raise

        except Exception as e:
            raise e

        return status, computer


    def _validate_informations(self, inventory_number, request_host):
        try:
            status = 7
            _info = self._search_by_inventory_number(inventory_number)
            try:
                _glpi_info = self._search_in_glpi_by_inventory_number(inventory_number)
            except:
                raise AssertionError('GLPI server is not responding')

            count = 0
            for computer in _glpi_info.values():
                if computer['computer_ipaddress'] == request_host:
                    count += 1

            glpi_id = _glpi_info[1]['computer_id']
            if count == 0:
                query = f"insert into computers_logs(`type_id`, `computer_id`, `body`) values (4, {glpi_id}, 'IP information does not match')"
                Database().commit_without_return(query)
                status = 4
            
            if _glpi_info[1]['computer_name'] != _info[1]['computer_name']:
                status = 1
            
            if _info[1]['status_id'] != status and _info[1]['status_id'] != 2:
                query = f'UPDATE `computers` SET `status_id` = {status} WHERE `inventory_number`= {inventory_number};'
                Database().commit_without_return(query)

            print(_info[1]['status_id'])

        except Exception as e:
            raise e

        return status, _glpi_info


    def _update_status_of_computer(self, inventory_number, status):
        try:
            query = f'UPDATE `computers` SET `status_id` = {status} WHERE `inventory_number`= {inventory_number};'
            Database().commit_without_return(query)
        except Exception as e:
            raise e

        return True