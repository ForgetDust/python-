# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:53:32 2020

@author: tute
"""

import socket
from threading import *

PORT = 65522
HOST = '192.168.13.32'


def send(sock,addr):
    i_say = ''
    sock.sendto(i_say.encode('utf-8').addr)
    
def recv(sock):
    while True:
        other_say,addr = sock.recvfrom(1024)
        print('{} say> {}'.format(addr[0], other_say.decode('utf-8')))
        
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))
    ipaddr = input('you want to say(ip):')
    addr = (ipaddr,65522)
    
    sendTH = Thread(target=recv,args = (s,addr))
    sendTH.setDaemon(True)
    sendTH.start()
    recvTH = Thread(target = recv,args = (s,))
    recvTH.setDaemon(True)
    recvTH.start()
    sendTH.join()
    recvTH.join()    