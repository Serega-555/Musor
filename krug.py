import turtle as t

def circle():
    t.penup()
    t.goto(0, 0)
    n = 30
    for i in range(3):
        for j in range(n):
            t.pendown()
            t.forward(360 / n)
            t.left(360 / n)
        for j in range(n):
            t.pendown()
            t.forward(360 / n)
            t.right(360 / n)

circle()