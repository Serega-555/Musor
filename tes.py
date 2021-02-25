# Работа с библиотекой turtle (черепашка) через функцию def:

import turtle as t
import math


def square(n, pix):
    # R = pix / (2 * math.sin(math.radians(360 / (2 * n))))
    
    t.goto(0,0)
    for j in range(n):
        t.forward(pix)
        t.left(360 / n)
        

square(10, 40)