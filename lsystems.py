import turtle, math

turtle.screensize(2000, 2000)

def draw_tree(number_of_iterations, angle):
    turtle.left(90)
    step = number_of_iterations*2
    i = 1
    positions = []
    new_positions = []
    turtle.forward(step)
    positions.append([turtle.pos(), turtle.heading()])
    while i <= number_of_iterations and step > 10:
        step = math.floor(step/i)
        for position in positions:
            turtle.penup()
            turtle.goto(position[0])
            turtle.setheading(position[1]+angle)
            turtle.pendown()
            turtle.forward(step)
            new_positions.append([turtle.pos(), turtle.heading()])
            turtle.penup()
            turtle.goto(position[0])
            turtle.setheading(position[1]-angle)
            turtle.pendown()
            turtle.forward(step)
            new_positions.append([turtle.pos(), turtle.heading()])
        positions = new_positions
        new_positions = []
        i += 1

    turtle.hideturtle()

##draw_tree(100, 15)

axiom = 'F'
constants = ['l', 'r']
rules = {'F':'FlFrFrFlF'}
drawing_rules = {'F':(turtle.forward, 10), 'l':(turtle.left, 90), 'r':(turtle.right, 90)}

def LS(axiom, rules, constants, drawing_rules, number_of_iterations):
    for i in range(number_of_iterations):
        print(axiom)
        new = ''
        for character in axiom:
            if character not in constants:
                new += rules[character]
            else:
                new += character
        axiom = new
        new = ''
    for char in axiom:
        drawing_rules[char][0](drawing_rules[char][1])

LS(axiom, rules, constants, drawing_rules, 3)
    
