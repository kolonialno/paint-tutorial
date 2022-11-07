from turtle import *
from random import *

ts = Screen()
ts.screensize(canvwidth=595, canvheight=842, bg="light blue")

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

turtles = [t1, t2, t3, t4]


def branch(t, branch_length):
    angle = randint(22, 30)
    sf = uniform(0.6, 0.8)
    size = int(branch_length / 10)
    t.pensize(size)
    if branch_length < 20:
        t.color('green')
        t.stamp()
        t.color('brown')
    if branch_length > 10:
        t.forward(branch_length)
        t.left(angle)
        branch(t, branch_length * sf)
        t.right(angle * 2)
        branch(t, branch_length * sf)
        t.left(angle)
        t.backward(branch_length)


x = -300

for t in turtles:
    t.speed(1000)
    t.left(90)
    t.color('brown')
    t.pu()
    x += randint(80, 160)
    t.goto(x, randint(-100, 100))
    t.pd()
    branch(t, 100)

ts.getcanvas().postscript(file="tree.eps", height=842, width=595)
