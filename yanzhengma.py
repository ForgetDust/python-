# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : yanzhengma.py
@Author : ForgetDust
@Time : 2020/9/8 10:22
"""

import random


def yzm(check_num=4):
    temp = ''
    for i in range(check_num):                          # check_num为需要循环的次数，也就是需要生成验证码的个数，默认为4
        choice = random.randint(1, 3)                   # 生成1到3的随机数
        if choice == 1:                                 # 如果choice为1，则随机验证码的值为数字
            temp += random.choice('0123456789')
        elif choice == 2:                               # 如果choice为2，则随机验证码的值为大写字母
            num = random.randint(65, 90)
            temp += chr(num)
        elif choice == 3:                               # 如果choice为3，则随机验证码的值为小写字母
            num = random.randint(97, 122)
            temp += chr(num)
    return temp

s = int(input('请输入需要生成的验证码位数：'))

a = yzm(s)
print('验证码为：%s' %(a,))