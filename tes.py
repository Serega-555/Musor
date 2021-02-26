# Работа с библиотекой turtle (черепашка) через функцию def:

import turtle as t
import math
# R = pix / (2 * math.sin(math.radians(360 / (2 * n))))

def square():
    m = 5
    n = 3
    pix = 20
    for i in range(m):
        R = pix / (2 * math.sin(math.radians(360 / (2 * n))))
        t.penup()
        t.goto(R, R)
        print(R)
        for j in range(n):

            t.pendown()
            t.forward(pix)
            t.left(360 / n)
        n += 1
        pix += 10
square()