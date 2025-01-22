# 

import turtle

colors = ['#4e00bb', '#747ba1', '#e3a58a', '#e7d2cc', '#69868a', '#cdd1c9']
cursor = turtle.Pen()
turtle.bgcolor('black')
cursor.speed("fastest")
for x in range (1080):
    cursor.pencolor(colors[x%6])
    cursor.width(x//100 + 1)
    cursor.forward(x)
    cursor.left(59)

turtle.done()
