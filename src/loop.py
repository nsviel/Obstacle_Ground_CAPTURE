#---------------------------------------------
from param import param_py

from HTTPS import https_server
from SOCK import sock_client
from perf import perf_throughput
from perf import perf_client_network
from perf import perf_server_network

from src import connection
from src import state
from src import capture
from src import parser_json
from src import device
from src import terminal

import time


#Main function
def program():
    # Init variables
    init()

    # Start main loop program
    while param_py.run_loop:
        loop()

    # Join threads
    end()

#Sub-function
def init():
    state.load_configuration()
    sock_client.connection()
    connection.start_daemon()
    https_server.start_daemon()
    perf_throughput.start_daemon()
    perf_client_network.start_daemon()
    perf_server_network.start_daemon()
    terminal.addLog("OK", "Program initialized")

def loop():
    time.sleep(1)

def end():
    terminal.addLog("OK", "Program ending ...")
    parser_json.upload_file(param_py.path_state_py, param_py.state_py)
    connection.stop_daemon()
    https_server.stop_daemon()
    perf_throughput.stop_daemon()
    perf_client_network.stop_daemon()
    perf_server_network.stop_daemon()
    terminal.shutdown()
