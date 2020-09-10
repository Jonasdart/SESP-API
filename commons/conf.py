#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

import configparser

def sesp_server():
    config = configparser.ConfigParser()
    config.read('resources\\models\\commons\\conf.cfg')

    debug = config.get('sesp_server', 'debug')
    bind_address = config.get('sesp_server', 'bind_address')
    bind_port = config.get('sesp_server', 'bind_port')

    return {
        'address' : bind_address,
        'port'    : port,
        'debug'   : debug
    }


def fusion_inventory():
    config = configparser.ConfigParser()
    config.read('resources\\models\\commons\\conf.cfg')

    server = config.get('fusion_inventory', 'server')
    inventory_frequency = config.get('fusion_inventory', 'inventory_frequency')

    return {
        'server' : server,
        'inventory_frequency'    : int(inventory_frequency),
    }