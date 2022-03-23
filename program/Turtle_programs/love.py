'''import turtle


star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()



'''
# from turtle import *
import turtle

pen = turtle.Turtle()


def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)


def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()


def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write("I LOVE ME", font=("verdana", 12, "bold"))
heart()
txt()
pen.ht()



# turtle.done()
