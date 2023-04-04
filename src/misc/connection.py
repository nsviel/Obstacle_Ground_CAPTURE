#---------------------------------------------
from src.param import param_capture
from src.SOCK import sock_client
from src.interface import lidar
from src.misc import parser_json
from src.interface import device
from src.misc import terminal
from src.HTTPS import https_client_con
import threading
import socket
import time


def start_daemon():
    try:
        thread_con = threading.Thread(target = thread_test_connection)
        thread_con.start()
        terminal.addDaemon("#", "ON", "Connection tests")
    except:
        pass

def stop_daemon():
    param_capture.run_thread_con = False
    terminal.addDaemon("#", "OFF", "Connection tests")

def thread_test_connection():
    param_capture.run_thread_con = True
    while param_capture.run_thread_con:
        # Test connections
        https_client_con.test_hu_con()
        lidar.test_connection()
        device.update_list()

        # Update state
        parser_json.upload_state()
        update_nb_thread()

        # Wait for 1 second
        time.sleep(param_capture.tic_connection)

def get_ip_adress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def update_nb_thread():
    param_capture.state_capture["self"]["nb_thread"] = threading.active_count()

def check_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    is_open = False
    if result == 0:
       is_open = True
    else:
        terminal.addLog("error", "Port \033[1;32m%d\033[0m is closed"% port)
    sock.close()
    return is_open;
