#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

from resources.models.commons.glpi import Glpi
import requests

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
                raise Exception('Nenhum Resultado Encontrado')
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
                raise Exception('Nenhum Resultado Encontrado')
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
                request = f'http://{computer_ipaddress}:62354/now'
                response = requests.get(request)
                
                if response.status_code != 200:
                    raise Exception('Error during request new inventory by http server.')

        except Exception as e:
            raise e      


    def _schedule_next_reboot(self, inventory_number, now=False):
        raise NotImplementedError


    def _schedule_next_shutdown(self, inventory_number, now=False):
        raise NotImplementedError