import os, socket, sys, configparser
from classes.SocketServer import SocketServer

# Configuration Parser Setup
try:
    parser = configparser.ConfigParser()
    parser.read("config.conf")
except:
    print("Cannot load config.conf file.")

# IP / PORT
host = socket.gethostname()
port = int(parser.get("server", "port"))

ss = SocketServer(socket, port)
ss.run()