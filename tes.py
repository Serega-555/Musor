# Работа с библиотекой turtle (черепашка) через функцию def:

import turtle as t
import math


def square(n, pix):

    for j in range(n):
        R = pix / (2 * math.sin(math.radians(360 / (2 * n))))
        t.penup()
        t.goto(-R, -R)
        for jj in range(3, n + 1, 1):
            t.pendown()
            t.forward(pix)
            t.left(360 / jj)
        

square(10, 40)