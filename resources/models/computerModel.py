#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

class ComputerModel():
    
    
    def _search_in_glpi_by_name(self, name):
        raise NotImplementedError

    
    def _search_in_glpi_by_inventory_number(self, inventory_number):
        raise NotImplementedError


    def _search_in_glpi_by_ip_address(self, ip_address):
        raise NotImplementedError


    def _change_status(self, inventory_number, status):
        raise NotImplementedError


    def _change_status_in_glpi(self, inventory_number, status):
        raise NotImplementedError


    def _change_name_in_glpi(self, inventory_number, name='default'):
        raise NotImplementedError

    
    def _schedule_next_inventory(self, inventory_number, now=False):
        raise NotImplementedError


    def _schedule_next_reboot(self, inventory_number, now=False):
        raise NotImplementedError


    def _schedule_next_shutdown(self, inventory_number, now=False):
        raise NotImplementedError