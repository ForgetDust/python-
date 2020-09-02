# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : hero.py
@Author : ForgetDust
@Time : 2020/9/1 11:20
"""

hp = 100

print('welcome Heroes World！')
print("|the world is like this #####,'a' for left,'d' for right |")

name = input('input your name:')

if not name:
    name = '玩家1'

usrmsg = [name,hp]

print("your hero name is:",usrmsg[0],'Hp is',usrmsg[1])
print("and now you are here: * #### | 'a' for left,'d' for right |")

userinput = input()

if userinput == 'd':
    print("you are here # * ###")

if userinput == 'a':
    print("you are here * ####")
