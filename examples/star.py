from turtle import *

speed(100)

color('red', 'yellow')

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

turtles = [t1, t2, t3, t4]

for t in turtles:
    star(t)


def star(turt):
    
    begin_fill()
    while True:
        turt.forward(200)
        turt.left(170)
        if abs(pos()) < 1:
            break
    end_fill()


star()

done()
