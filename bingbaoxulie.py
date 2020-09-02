# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : bingbaoxulie.py
@Author : ForgetDust
@Time : 2020/9/2 14:15
"""

ac = input('please input a number:')

while not ac.isdigit():
    print('please input a int!')
    ac = input('please input a number:')

ac = int(ac)
while ac != 1:
    if ac % 2 == 0:
        ac = ac/2
    else:
        ac = (ac * 3) + 1
    print(ac)
