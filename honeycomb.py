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
tortoise.color('#FFBD33')

# l-system settings
generations = 20
axiom = 'A'
character_1, rule_1 = 'A', 'AB'
character_2, rule_2 = 'B', 'A'
step = 50
angle = 60


def apply_rules(axiom):
    return ''.join([rule_1 if character == character_1 else rule_2 for character in axiom])


def get_result(generations, axiom):
    for generation in range(generations):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 + 60)
turtle.clear()
turtle.write(f'generation: {generations}', font=("Courier New", 20, "bold"))

axiom = get_result(generations, axiom)
for character in axiom:
    if character == character_1:
        tortoise.left(60)
        tortoise.forward(step)
    elif character == character_2:
        tortoise.right(60)
        tortoise.forward(step)
    
screen.exitonclick()
