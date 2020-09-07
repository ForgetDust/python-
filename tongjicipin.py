# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:33:35 2020

@author: tute
"""

contents = open('KMSWHS.txt','r').read()
list_songs = contents.split()

def tolet(contents):
    s = {}
    for i in contents:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1
            
    return s

a = tolet(list_songs)

print(a)