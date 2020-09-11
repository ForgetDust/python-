# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:13:44 2020

@author: tute
"""

#client

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",65532))
s.send(b"hello i an client!!!")

data = s.recv(1024)
print("Server say: %s" % data.decode())
s.close()