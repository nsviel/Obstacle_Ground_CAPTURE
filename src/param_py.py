#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# Thread
run_loop = True;
run_thread_con = False

# Parameter
gui_width = 600;
gui_height = 750;
with_geolocalization = False

# Connection
pywardium_ip = "127.0.0.1"
http_connected = False
socket_connected = False
ssd_connected = False

# State
geo_country = "France"
socket = None

# Path
path_ssd = "/media/" + os.getlogin() + "/lidar_ssd"

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
