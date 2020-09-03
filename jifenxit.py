# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:46:30 2020

@author: ForgetDust
"""

team1 = input('please input team1 name:')
team2 = input('please input team2 name:')


list_score1 = []
list_score2 = []

totle1 = 0
totle2 = 0

user = ''

while user != 'game over':
    user = input('please input team:')
    if user == team1:
        score1 = int(input('please input score:'))
        list_score1.append(score1)
        for i in range(0,len(list_score1)):
            totle1 = totle1 + list_score1[i]
            print('team %s is scored %d   team %s is scored %d' %(team1,totle1,team2,totle2))
    if user == team2:
        score2 = int(input('please input score:'))
        list_score2.append(score2)
        for o in range(0,len(list_score2)):
            totle2 = totle2 + list_score2[o]
            print('team %s is scored %d   team %s is scored %d' %(team1,totle1,team2,totle2))
else:
    print('team %s scored %d' %(team1,totle1))
    print('team %s scored %d' %(team2,totle2))
    if totle1 > totle2:
        print('Winer is %s' %team1)
    elif totle1 < totle2:
        print('Winer is %s' %team2)
    else:
        print("it ends in a draw")
        
