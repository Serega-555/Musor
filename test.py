import turtle as t

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



pix = int(input("Введите длину в пикселях "))
n = int(input("Введите колличество лапок "))
grad = 360 / n
for j in range(n):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(pix)
    t.stamp()
    t.left(grad)







# pix = 100
# t.shape("turtle")
# t.goto(0, 0)
# t.forward(pix)
# t.left(180)

# t.stamp()
# t.penup()
# t.goto(0, 0)
# t.pendown()
# t.right(90)
# t.forward(pix)
# t.stamp()

# t.penup()
# t.goto(0, 0)
# t.pendown()
# t.left(90)
# t.forward(pix)
# t.stamp()

# t.penup()
# t.goto(0, 0)
# t.pendown()
# t.right(90)
# t.backward(pix)
# t.stamp()

