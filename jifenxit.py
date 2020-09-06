# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : jifenxit.py
@Author : ForgetDust
@Time : 2020/9/3 16:51
"""


team1 = input('please input team1 name:').strip()                   #输入第一支球队队名，去除字符串前后空格
if team1 == 'game over':                                            #判断球队名称是否为game over，是则要求重新输入
    team1 = input('please input team1 name:').strip()

team2 = input('please input team2 name:').strip()                       #输入第二支球队队名，去除字符串前后空格
if team2 == 'game over':                                                #判断球队名称是否为game over，是则要求重新输入
    team2 = input('please input team2 name:').strip()

if team1 == team2:                                                      #判断两只球队名称是否相同，相同则要求重输
    team2 = input('please input another team2 name:').strip()

#定义得分列表
list_score1 = []
list_score2 = []

#定义初始分值
totle1 = 0
totle2 = 0

#定义用户输入初始值为空
user = ''

while user != 'game over':                                          #判断，当用户输入值不为game over时，执行以下条件
    user = input('please input team:').strip()                      #输入球队名称
    if user == team1:                                               #判断用户输入球队如果是team1，则执行本条判断语句下的条件
        score1 = input('please input score:').strip()               #对用户输入分值做去除前后空格处理
        if score1.isdigit() == True:                                #判断用户输入的分值是否为纯数字
            score1 = int(score1)                                    #转换用户输入的分值为int整型
            if score1 <= 3:                                         #判断用户输入最大得分不允许超过3分
                list_score1.append(score1)                          #将得分存入得分列表
                totle1 = sum(list_score1)                           #对列表内的所有数值求和
                print('team %s is scored %d   team %s is scored %d' % (team1, totle1, team2, totle2))               #格式化输出两队得分情况
            else:
                print('The score you entered is illegal')           #用户输入得分大于3的情况下提示输入字符非法并返回重新输入
        else:
            print('The score you entered is illegal')               #用户输入得分非纯数字情况下返回输入非法并返回要求重新输入

    elif user == team2:
        score2 = input('please input score:').strip()
        if score2.isdigit() == True:
            score2 = int(score2)
            if score2 <= 3:
                list_score2.append(score2)
                totle2 = sum(list_score2)
                print('team %s is scored %d   team %s is scored %d' % (team1, totle1, team2, totle2))
            else:
                print('The score you entered is illegal')
        else:
            print('The score you entered is illegal')

    elif user != 'game over':                       #判断用户输入的队伍名称非已存在的两队名称，且不是结束比赛命令时，返回队伍未被创建错误，并要求重新输入
        print('The team you entered does not exist,Please re-enter!')

else:                                   #条件判断为用户输入game over时，打印GAME　OVER　并同时打印两队总得分成绩和最终获胜队伍名称，如果得分相同则打印平局
    print("GAME OVER!")
    print('team %s scored %d' % (team1, totle1))
    print('team %s scored %d' % (team2, totle2))
    if totle1 > totle2:
        print('Winer is %s' % team1)
    elif totle1 < totle2:
        print('Winer is %s' % team2)
    else:
        print("it ends in a draw")