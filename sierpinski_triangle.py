import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle. Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# turtle settings
tortoise = turtle.Turtle()
tortoise.pensize(3)
tortoise.speed(0)
tortoise.setpos(-WIDTH // 3, -HEIGHT // 2)
tortoise.color('#228B22')

# l-system settings
generations = 7
axiom = 'F'
character_1, rule_1 = 'F', 'F-G+F+G-F'
character_2, rule_2 = 'G', 'GG'
step = 8
angle = 120


def apply_rules(axiom):
    return ''.join([rule_1 if character == character_1 else
                    rule_2 if character == character_2 else
                    character for character in axiom])


def get_result(generations, axiom):
    for generation in range(generations):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {generations}', font=("Courier New", 20, "bold"))

axiom = get_result(generations, axiom)
for character in axiom:
    if character == character_1 or character == character_2:
        tortoise.forward(step)
    elif character == '+':
        tortoise.right(angle)
    elif character == '-':
        tortoise.left(angle)
    
screen.exitonclick()
