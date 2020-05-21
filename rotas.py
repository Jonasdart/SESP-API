#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'


from flask import Flask, jsonify, request
from model import Backend
import configparser

app = Flask(__name__)
backend = Backend()


def bind_server():
    config = configparser.ConfigParser()
    config.read('conf.cfg')

    server_host = config.get('config_server', 'bind_address')
    server_port = config.get('config_server', 'bind_port')

    return [server_host, server_port]


@app.route('/get_computer', methods=['POST'])
def get_computer():
    try:
        data = request.get_json()
        if len(data) > 2:
            e = 'Request out of params'
            raise Exception(e)
        
        response = backend.return_resume_of_computer(data)
        if response['Status'] != 200:
            raise Exception(response)
        
    except Exception as e:
        response = {
            'Message' : {
                'Error' : str(e)
            },
            'Status' : 400
        }
    status = int(response['Status'])
    return jsonify(response), status

if __name__ == "__main__":
    server_address, server_port = bind_server() 
    app.run(host= server_address, port= server_port, debug=False)