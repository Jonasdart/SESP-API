#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'


class IncidentModel():


    def _search_incidents_by_name(self, name):
        raise NotImplementedError


    def _search_incidents_by_description(self, description):
        raise NotImplementedError


    def _search_incident_by_id(self, incident_id):
        raise NotImplementedError