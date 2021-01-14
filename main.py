# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:19:54 2021

@author: mahdi
"""


from tkinter import *

import screen_brightness_control as sbc

def set_brightness(args):
    try:
        sbc.set_brightness(args)
    except sbc.ScreenBrightnessError as error:
        print(error)
    
    
def slider():
    master = Tk()
    master.title('Screen_Brightness_Control')
    w = Scale(master, from_=0, to=100,tickinterval=5,length=600 ,
              orient=HORIZONTAL , command = set_brightness )
    w.set(sbc.get_brightness())
    w.pack()    
    mainloop()

slider()