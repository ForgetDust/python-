# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from threading import *
import subprocess
from queue import *


queue5 = Queue()
ips = ['192.168.13.33',
       '192.168.13.25',
       '192.168.13.55',
       '192.168.13.64',
       '192.168.13.42',
       '192.168.13.22',
       '192.168.13.35']

def ip_ping(i,q):
    while True:
        ip = q.get()
        print("Thread %s : Ping %s :" % (i,ip))
    
        #Windows
        ret = subprocess.call('ping -c  %s ' % ip,
                              shell = True,
                              stdout = open('NUL','w'),
                              stderr = subprocess.STDOUT)
        
        if ret == 0:
            print("%s :is alive" % ip)
        else:
            print('%s :did not respond' % ip)
            
        q.task_done()
        
for i in range(3):
    th = Thread(target=ip_ping,args= (i,queue5))
    th.setDaemon(True)
    th.start()

for ip in ips:
    queue5.put(ip)
    
print("Main Thread waitiong.....")
queue5.join()
print('Done')