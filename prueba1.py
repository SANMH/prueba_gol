# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:27:54 2018

@author: ESFOT
"""

import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 800, height = 600)
canvas.pack()


my_image = PhotoImage(file = "1.gif")  
canvas.create_image(0, 0, anchor=NW, image = my_image)

my_image2 = PhotoImage(file = "2.gif")  
canvas.create_image(50, 100, anchor=NW, image = my_image2)

my_image3 = PhotoImage(file = "3.gif")  
canvas.create_image(200, 300, anchor=NW, image = my_image3)



def moverkame(event):
    canvas.move (3, 10, 0) # primer numero es la imagen , segundo es la velocidad de desplazamiento, tercero es el angulo de inclinacion
    
canvas.bind_all("<KeyPress-Right>", moverkame)


def moverkame1(event):
    canvas.move (3, -10, 0)
    # primer numero es la imagen , segundo es la velocidad de desplazamiento, tercero es el angulo de inclinacion
    print("se marco un gol")
canvas.bind_all("<KeyPress-Left>", moverkame1)



      
tk.mainloop()

