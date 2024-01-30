import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('black')

# turtle settings
tortoise = turtle.Turtle()
tortoise.pensize(5)
tortoise.speed(10)
tortoise.color('white')

for i in range(0, 900, 10):
    tortoise.forward(i)
    tortoise.right(90)

turtle.Screen().exitonclick()
