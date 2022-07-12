#! /usr/bin/python
#---------------------------------------------

from param import param_py

from src import device
from src import socket
from src import io

from threading import Thread

import pcapy


def start_lidar_capture():
    thread_l1 = Thread(target = start_l1_capture)
    thread_l2 = Thread(target = start_l2_capture)
    thread_l1.start()
    thread_l2.start()

def stop_lidar_capture():
    param_py.run_thread_l1 = False
    param_py.run_thread_l2 = False

def start_l1_capture():
    connected = param_py.state_py["lidar_1"]["connected"]
    device = param_py.state_py["lidar_1"]["device"]
    if(connected):
        device_ok = device.check_if_device_exists(device)
        if(device_ok):
            param_py.state_py["lidar_1"]["nb_packet"] = 0
            listener = pcapy.open_live(device , 1248 , 1 , 0)
            param_py.run_thread_l1 = True
            while param_py.run_thread_l1:
                (header, packet) = listener.next()
                if(len(packet) == 1248):
                    socket.send_packet(packet)
                    param_py.state_py["lidar_1"]["nb_packet"] += 1

def start_l2_capture():
    connected = param_py.state_py["lidar_2"]["connected"]
    device = param_py.state_py["lidar_2"]["device"]
    if(connected):
        device_ok = device.check_if_device_exists(device)
        if(device_ok):
            param_py.state_py["lidar_2"]["nb_packet"] = 0
            param_py.run_thread_l2 = True
            listener = pcapy.open_live(device , 1248 , 1 , 0)
            while param_py.run_thread_l2:
                (header, packet) = listener.next()
                if(len(packet) == 1248):
                    socket.send_packet(packet)
                    param_py.state_py["lidar_2"]["nb_packet"] += 1