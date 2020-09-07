# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : hero.py
@Author : ForgetDust
@Time : 2020/9/1 11:20
"""
import numpy

welcome = '- * - welcome to Hearoes World ! - * -'
#地图信息
mapmsg = '####### \n ####### \n #######'
mapins = "\n- * - the world is like this - * - \n %s \n the '*' is you" %(mapmsg,)
worldMap = [['#','#','#','#','#','#','#'],['#','#','#','#','#','#','#'],['#','#','#','#','#','#','#']]

instruction = '''
contrl your hero : | 'a' for left | 'd' for right | 'w' for up | 's' for down| '''

print(welcome)


hp = 100
name = input('input your name:')

if not name:
    name = '玩家1'

usermsg = {'name':name,'hp':hp}

print("Hi!",usermsg['name'],'you Hp is :',usermsg['hp'])
print(mapins,instruction)

x = 0
y = 0

while 1 :
    worldMap[x][y] = "*"
    print('you are here\n'," ".join(worldMap[0]))
    print(" ".join(worldMap[1]))
    print(" ".join(worldMap[2]))
          
    userinput = input('go or quit:')
    
    if userinput == 'd' and x < 6:
        worldMap[x][y] = '#'
        y += 1
    
    elif userinput == 'a' and x > 0:
        worldMap[x][y] = '#'
        y -= 1
    
    elif userinput == 'w' and  x > 0:
        worldMap[x][y] = '#'
        x -= 1 
        
    elif userinput == 's' and x < 2:
        worldMap[x][y] = '#'
        x += 1
        
    elif userinput == 'quit':
        print('good bye !!')
        break
    else:
        print(instruction)