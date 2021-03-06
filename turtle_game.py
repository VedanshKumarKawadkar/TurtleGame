import turtle
import random

die = [1, 2, 3, 4, 5, 6]
turtle.bgcolor('Black')
t = turtle.Turtle()
t.penup()
t.goto(500, 100)
t.pendown()
t.pen(pencolor='purple', pensize=8, fillcolor='purple')
t.rt(90)
t.fd(200)
player1 = turtle.Turtle()
player1.color('Red')
player1.shape('turtle')
player1.shapesize(2)
player1.penup()
player1.goto(-500, 100)
player2 = player1.clone()
player2.color('Blue')
player2.shape('turtle')
player2.penup()
player2.goto(-500, -100)
player1.goto(500, 100)
player1.pendown()
player1.dot(20)
player1.penup()
player1.goto(-500, 100)
player2.goto(500, -100)
player2.pendown()
player2.dot(20)
player2.penup()
player2.goto(-500, -100)
for i in range(20):
    if player1.pos() >= (500, 100):
        print('Player1 wins')
        break
    elif player2.pos() >= (500, -100):
        print('Player2 wins')
        break
    else:
        player1_turn = input('Press Enter to roll die.')
        die_outcome1 = random.choice(die)
        print('The die outcome is:')
        print(die_outcome1)
        print('Player1 moves', die_outcome1*10, 'steps')
        player1.fd(die_outcome1*10)
        print('Player2 turn')
        player2_turn = input('Press Enter to roll die.')
        die_outcome2 = random.choice(die)
        print('The die outcome is:')
        print(die_outcome2)
        print('Player2 moves', die_outcome2*10, 'steps')
        player2.fd(die_outcome2*10)
