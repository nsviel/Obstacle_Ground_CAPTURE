#! /usr/bin/python
#---------------------------------------------

from src import param_hu
from src import param_py

import json
import http.client as client


def test_connection():
    sock = client.HTTPConnection(param_hu.hubium_ip, param_hu.hubium_http_port, timeout=1)
    try:
        sock.request("GET", "/test")
        param_py.http_connected = True
    except:
        connection_closed()
    sock.close()

def connection_closed():
    param_py.http_connected = False
    param_py.mqtt_connected = False
