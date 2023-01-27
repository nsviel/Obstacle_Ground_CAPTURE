#---------------------------------------------
# Terminal output functions
#---------------------------------------------
import time


def addLog(type, message):
    if(type == "#"):
        print("[\033[1;34m#\033[0m]     "+ message)
    elif(type == "OK"):
        print("[\033[1;32mOK\033[0m]    "+ message)
    elif(type == "error"):
        print("[\033[1;31merror\033[0m] "+ message)
    time.sleep(0.05)

def addDaemon(type, status, message):
    if(type == "#"):
        print("[\033[1;34m#\033[0m]     Daemon ", flush=True, end='')
    elif(type == "OK"):
        print("[\033[1;32mOK\033[0m]    Daemon ", flush=True, end='')
    elif(type == "error"):
        print("[\033[1;31merror\033[0m] Daemon ", flush=True, end='')

    if(status == "ON"):
        print("\033[1;32m"+status+"\033[0m - "+message)
    elif(status == "OFF"):
        print("\033[1;31m"+status+"\033[0m - "+message)

    time.sleep(0.05)

def shutdown():
    print("[\033[1;34m#\033[0m]     Program shutdown", flush=True, end='')
    print("...2", flush=True, end='')
    time.sleep(1)
    print("...1", flush=True)
    time.sleep(1)
