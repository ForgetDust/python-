# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : caushuzi.py
@Author : ForgetDust
@Time : 2020/9/2 11:20
"""

import random

s = random.randint(1,100)
count = 0
a = int(input('please input a number you gest in five chance:'))
while a != s:
    count = count+1
    if a >= s and count < 5:
        a = int(input("sorry! you are worry!it's too large please try again:"))
    elif a <= s and count < 5:
        a = int(input("sorry! you are worry!it's too small,please try again:"))
    else:
        print('sorry! you have no chance')
        break
else:
    print('你真辛运！猜对了')
