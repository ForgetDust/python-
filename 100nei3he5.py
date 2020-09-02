# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : suanfa.py
@Author : ForgetDust
@Time : 2020/9/2 11:01
"""

s=0
for i in range(1,101):
    if i % 3 == 0 or i % 5 ==0:
        s = s + i
        print(s)