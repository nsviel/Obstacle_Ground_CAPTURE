#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu

from src import socket
from src import http
from src import http_get
from src import saving
from src import lidar
from src import capture

from gui import scheme_link

from threading import Thread

import time


def thread_test_connection():
    while param_py.run_thread_con:
        http.test_connection()
        socket.test_socket_connection()
        http_get.get_state()
        saving.test_is_ssd()
        scheme_link.update_link_color()
        time.sleep(1)
        pass

def thread_test_lidar():
    while param_py.run_thread_con:
        lidar.test_lidar_connection()
        time.sleep(2)
        pass

def start_thread_test_conn():
    param_py.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

    thread_lid = Thread(target = thread_test_lidar)
    thread_lid.start()

def stop_thread():
    param_py.run_thread_con = False
    capture.stop_lidar_capture()

def parse_state_json():
    param_hu.mqtt_connected = param_hu.hubium_json["mqtt"]["connected"]
    param_hu.velo_connected = param_hu.hubium_json["velodium"]["connected"]
    param_hu.vale_connected = param_hu.hubium_json["valeo"]["connected"]
    param_hu.edge_connected = param_hu.hubium_json["edge"]["connected"]
    param_hu.ai_connected = param_hu.hubium_json["ai"]["connected"]
