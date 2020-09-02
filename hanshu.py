# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : hanshu.py
@Author : ForgetDust
@Time : 2020/9/1 15:44
"""
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)
y = np.sin(x)
plt.plot(x,y)
plt.show()

'''
'''
d = 'bad luck'
tihuan = d.replace("bad","good")

ip = '192.168.1.3'
ip.split('.')
'''
''''
import random
i = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

b = random.choice([i])
print(b)
'''
a = int(input('please input a number:'))
c = input('please input math way:')
b = int(input('please input another number:'))

if "+" in c:
    s = a+b
    print(s)
elif "-" in c:
    s = a-b
    print(s)
elif "*" in c:
    s = a*b
    print(s)
elif "/" in c:
    s = a/b
    print(s)
else:
    print("math way only allow:+ - * /")
