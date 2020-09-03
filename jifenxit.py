# ！/usr/bin/env python3
# -*- coding = utf-8 -*-

"""
@File : jifenxit.py
@Author : ForgetDust
@Time : 2020/9/3 16:51
"""


team1 = input('please input team1 name:').strip()
if team1 == 'game over':
    team1 = input('please input team1 name:').strip()

team2 = input('please input team2 name:').strip()
if team2 == 'game over':
    team2 = input('please input team2 name:').strip()

if team1 == team2:
    team2 = input('please input another team2 name:').strip()

list_score1 = []
list_score2 = []

totle1 = 0
totle2 = 0

user = ''

while user != 'game over':
    user = input('please input team:').strip()
    if user == team1:
        score1 = input('please input score:').strip()
        if score1.isdigit() == True:
            score1 = int(score1)
            if score1 <= 3:
                list_score1.append(score1)
                totle1 = sum(list_score1)
                print('team %s is scored %d   team %s is scored %d' % (team1, totle1, team2, totle2))
            else:
                print('The score you entered is illegal')
        else:
            print('The score you entered is illegal')

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

    elif user != 'game over':
        print('The team you entered does not exist,Please re-enter!')

else:
    print("GAME OVER!")
    print('team %s scored %d' % (team1, totle1))
    print('team %s scored %d' % (team2, totle2))
    if totle1 > totle2:
        print('Winer is %s' % team1)
    elif totle1 < totle2:
        print('Winer is %s' % team2)
    else:
        print("it ends in a draw")