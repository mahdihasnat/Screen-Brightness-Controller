# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:19:54 2021

@author: mahdi
"""


from tkinter import Tk, Scale, HORIZONTAL, mainloop
import screen_brightness_control as sbc

def set_brightness(args):
    """
	Set the brightness of the screen.
    """
    try:
        sbc.set_brightness(args)
    except sbc.ScreenBrightnessError as error:
        print(error)


def slider():
    """
    Create a slider to control the brightness of the screen.
    """
    master = Tk()
    master.title('Screen_Brightness_Control')

    window = Scale(master, from_=0, to=100,tickinterval=5,length=600 ,
              orient=HORIZONTAL , command = set_brightness )

    window.set(sbc.get_brightness())
    window.pack()
    mainloop()

slider()
