import turtle

turtle.bgcolor("black")

p = turtle.Pen()

p.pencolor("red")
p.width(3)
x_cord =0

for i in range(3,10):

    for j in range (i):
        degree = 360 / i
        p.left(degree)
        p.forward(100)

    p.up()

    p.down()
turtle.done()

turtle.done()


