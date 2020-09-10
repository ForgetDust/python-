# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter
import turtle
root = tkinter.Tk()

menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu,tearoff = 0)
submenu.add_command(label = "Open")
submenu.add_command(label = "Save")
menu.add_cascade(label = "File",menu = submenu)
root.config(menu = menu)

label = tkinter.Label(root,text = "Hello")
label.pack()
button1 = tkinter.Button(root,text = "star")
button1.pack()

def wjx(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
        
button1.bind('<Button-1>',wjx)
root.mainloop()