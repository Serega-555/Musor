# Работа с библиотекой turtle (черепашка) через функцию def:

import turtle as t
import math


def square(n, pix):
    R = math.sin(18)
    print(math.degrees(R))
    # R = 40 / (2 * math.sin(math.degrees(360 / (2 * 10))))
    
#     t.goto(0,0)
#     for j in range(n):
#         t.forward(pix)
#         t.left(360 / n)
        

square(10, 40)