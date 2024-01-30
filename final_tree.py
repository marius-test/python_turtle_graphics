import turtle
from random import randint

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle. Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgpic('mars.gif')
# screen.bgcolor(0, 0, 0)
screen.update()
screen.delay(0)

# turtle settings
tortoise = turtle.Turtle()
tortoise.pensize(3)
tortoise.speed(0)
tortoise.penup()
tortoise.setpos(WIDTH // 6, -HEIGHT // 4 - 25)
tortoise.pendown()
tortoise.color('#228B22')

# l-system settings
generations = 13
axiom = 'XY'
character_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 90
angle = lambda: randint(0, 45)
stack = []
color = [0.35, 0.2, 0.0]
thickness = 20

def apply_rules(axiom):
    return ''.join([rule_1 if character == character_1 else
                    character for character in axiom])


def get_result(generations, axiom):
    for generation in range(generations):
        axiom = apply_rules(axiom)
    return axiom


"""
turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {generations}', font=("Courier New", 20, "bold"))
"""

axiom = get_result(generations, axiom)
tortoise.left(90)
tortoise.pensize(thickness)
for character in axiom:
    tortoise.color(color)
    if character == 'F' or character == 'X':
        tortoise.forward(step)
    elif character == '@':
        step -= 6
        color[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        tortoise.pensize(thickness)
    elif character == '+':
        tortoise.right(angle())
    elif character == '-':
        tortoise.left(angle())
    elif character == '[':
        angle_, position_ = tortoise.heading(), tortoise.pos()
        stack.append((angle_, position_, thickness, step, color[1]))
    elif character == ']':
        angle_, position_, thickness, step, color[1] = stack.pop()
        tortoise.pensize(thickness)
        tortoise.setheading(angle_)
        tortoise.penup()
        tortoise.goto(position_)
        tortoise.pendown()

screen.exitonclick()
