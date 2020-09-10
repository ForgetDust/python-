# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:09:06 2020

@author: tute
"""

from Herostart import *

msg = "欢迎来到英雄无敌的世界......"

if __name__ == "__main__":
    print(msg)
    kali = Hero('kali')
    boss = Element('boss')
    print("boss hp:",boss.hp)
    print("英雄发起攻击！")
    kali.hit(boss)
    print("boss hp:",boss.hp)