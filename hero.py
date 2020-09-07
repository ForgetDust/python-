# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : hero.py
@Author : ForgetDust
@Time : 2020/9/1 11:20
"""
welcome = '- * - welcome to Hearoes World ! - * -'
mapmsg = '#######'
mapins = "\n- * - the world is like this - * - \n %s \n the '*' is you" %(a,)

worldMap = ['#','#','#','#','#','#','#']
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

point = 0

while 1 :
    worldMap[point] = " * "
    print('you are here',"".join(worldMap))
    userinput = input('go or quit:')
    
    if userinput == 'd' and point < 6:
        worldMap[point] = '#'
        point += 1
    
    elif userinput == 'a' and point > 0:
        worldMap[point] = '#'
        point -= 1
    
    elif userinput == 'w' and point > 0:
        worldMap[point] = '#'
        point 
        
    elif userinput == 's' and point < 6:
        worldMap[point] = '#'
        point
        
    elif userinput == 'quit':
        print('good bye !!')
        break
    else:
        print(instruction)
