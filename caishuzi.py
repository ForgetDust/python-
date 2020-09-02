# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : caushuzi.py
@Author : ForgetDust
@Time : 2020/9/2 11:20
"""

import random

s = random.randint(1,100)
print(s)
a = int(input('please input a number you gest:'))
while a != s:
    if a >= s:
        a = int(input("sorry! you are worry!it's too large please try again:"))
    else:
        a = int(input("sorry! you are worry!it's too small,please try again:"))
else:
    print('你真辛运！猜对了')
