import socket
from .Flag import Flag

class SocketServer():
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        try:
            self.sock = socket.socket()
        except:
            print("Socket creation error.")

    def run(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        while True:
            c, addr = self.sock.accept()
            print(f"{Flag.FLAG_CONNECTION_REQ} %s", addr)
            c.send(f"{Flag.FLAG_OK}")
            c.close()

    def send(self, msg):
        pass

    def receive(self, msg):
        pass

    def broadcast(self, msg):
        pass