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
        score1 = input('please input score:')
        if score1.isdigit() == 'true':
            score1 = int(score1)
            if score1 <= 3:
                list_score1.append(score1)
                totle1 = sum(list_score1)
                print('team %s is scored %d   team %s is scored %d' %(team1,totle1,team2,totle2))
            else:
                print('The score you entered is illegal')
        else:
            print('The score you entered is illegal')
  
    elif user == team2:
        score2 = int(input('please input score:'))
        if score2.isdigit() == 'true':
            score2 = int(score2)
            if score2 <= 3:
                list_score2.append(score2)
                totle2 = sum(list_score2)
                print('team %s is scored %d   team %s is scored %d' %(team1,totle1,team2,totle2))
            else:
                print('The score you entered is illegal')
        else:
            print('The score you entered is illegal')
        
    else:
        print('your input error! please try again!')
        
else:
    print("GAME OVER!")
    print('team %s scored %d' %(team1,totle1))
    print('team %s scored %d' %(team2,totle2))
    if totle1 > totle2:
        print('Winer is %s' %team1)
    elif totle1 < totle2:
        print('Winer is %s' %team2)
    else:
        print("it ends in a draw")
        
