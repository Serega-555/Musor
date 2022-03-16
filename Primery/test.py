# Работа с библиотекой turtle (черепашка)

import turtle as t

# 10 вложенных квадратов.
# t.penup()
# x = -25
# y = -25
# pix = 50
# for i in range(10):
#     t.penup()
#     t.goto(x, y)
#     for j in range(4):
#         t.pendown()
#         t.forward(pix)
#         t.left(90)
#     x -= 10
#     y -= 10
#     pix += 50 / 100 * 40
#-----------------------------------------------------------
# Паучек
# pix = 100
# n = 15
# grad = 360 / n
# for j in range(n):
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     t.forward(pix)
#     t.stamp()
#     t.left(grad)

# Паучек второй вариант
# def square(n):
    
#     for j in range(n):
#         t.goto(n / 2, n / 2)
#         t.forward(n * 10)
#         t.left(360 / n)

# square(10)
#-----------------------------------------------------------
# Круг
# t.penup()
# t.goto(2, 2)
# n = 100
# for j in range(n):
#     t.pendown()
#     t.forward(360 / n)
#     t.left(360 / n)
#-----------------------------------------------------------
# Спираль
# t.goto(0, 0)
# n = 500
# for j in range(n):
#     t.forward(j / 15)
#     t.left(10)
#-----------------------------------------------------------
# квадратная «спираль
# t.goto(0, 0)
# n = 100
# for j in range(n):
#     t.forward(j * 3)
#     t.left(90)
#-----------------------------------------------------------

