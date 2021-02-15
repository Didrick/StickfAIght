import socket
import random

"""
100 => ask to connect
110 => ask random dice
200 => OK connect, followed by token after space
210 => OK follow by two random int separated by space
400 => Bad request
401 => KO connect, bad token
405 => KO method not allowed
409 => KO conflict token
500 => KO Internal Serveur Error
"""

import socket




class TCPClient:
    "TCP client"

    def __init__(self):
        #WIP : GUI change it
        self.HOST = '85.168.112.123'  # The server's hostname or IP address
        self.PORT = 65432        # The port used by the server

    def send(self,msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(msg.encode())
            data = s.recv(1024)
        print('Received', repr(data.decode()))

    def connect(self):
        self.send('100')





clt = TCPClient()
clt.connect()
