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
tortoise.pensize(4)
tortoise.speed(1)
tortoise.setpos(-WIDTH // 6, HEIGHT // 6)
tortoise.color('#ADD8E6')

# l-system settings
generations = 5
axiom = 'F++F++F'
character_1, rule_1 = 'F', 'F-F++F-F'
step = 600
angle = 60


def apply_rules(axiom):
    return ''.join([rule_1 if character == character_1 else character for character in axiom])


def get_result(generations, axiom):
    for generation in range(generations):
        axiom = apply_rules(axiom)
    return axiom


for generation in range(generations):
    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'generation: {generations}', font=("Courier New", 20, "bold"))

    tortoise.setheading(0)
    tortoise.goto(-WIDTH // 6, HEIGHT //6)
    tortoise.clear()

    length = step / pow(3, generation)
    for character in axiom:
        if character == character_1:
            tortoise.forward(length)
        elif character == '+':
            tortoise.right(angle)
        elif character == '-':
            tortoise.left(angle)
    
    axiom = apply_rules(axiom)

screen.exitonclick()
