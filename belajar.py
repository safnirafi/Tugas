import time
from turtle import *

pen= Turtle()
pen.color('red')
bgcolor('black')

def draw_heart(size):
    pen.color('red')
    pen.pensize(2)
    pen.pendown()
    pen.setheading(150)
    pen.begin_fill()
    pen.fd(size)
    pen.circle(size * -3.745, 45)
    pen.circle(size * -1.431, 165)
    pen.left(120)
    pen.circle(size * -1.431, 165)
    pen.circle(size * -3.745, 45)
    pen.fd(size)
    pen.end_fill()



draw_heart(62)
pen.ht()
done()