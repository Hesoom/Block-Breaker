from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from block import Block
import time

# Setup screen
screen = Screen()
screen.bgcolor("#1A1A1A")
screen.setup(width=650, height=650)
screen.title("Breakout")
screen.tracer(0)
screen.addshape("img/paddle.gif")
screen.addshape("img/red.gif")
screen.addshape("img/blue.gif")
screen.addshape("img/green.gif")
screen.addshape("img/yellow.gif")

ball = Ball()
paddle = Paddle((0,-250))

# Paddle smooth moving
right_pressed = False
left_pressed = False

def hold_right():
    global right_pressed
    right_pressed = True

def release_right():
    global right_pressed
    right_pressed = False

def hold_left():
    global left_pressed
    left_pressed = True

def release_left():
    global left_pressed
    left_pressed = False

screen.listen()
screen.onkeypress(hold_right, "Right")
screen.onkeyrelease(release_right, "Right")
screen.onkeypress(hold_left, "Left")
screen.onkeyrelease(release_left, "Left")

# Creating blocks
blocks = []
start_x = -220
start_y = 260
rows = 4
columns = 7
x_spacing = 70
y_spacing = 35
colors = ["img/blue.gif","img/red.gif","img/yellow.gif","img/green.gif"]
for row in range(rows):
    for col in range(columns):
        x = start_x + col * x_spacing
        y = start_y - row * y_spacing
        color = colors[row]
        block = Block(position=(x, y), color=color)
        blocks.append(block)

game_is_on = True
counter = 0
time_sleep = 0.005

while game_is_on:
    screen.update()
    time.sleep(time_sleep)
    ball.move()

    if right_pressed:
        paddle.move(1)
    if left_pressed:
        paddle.move(-1)

    # Detect collision with upper wall
    if ball.ycor() > 320:
        ball.bounce_y()
    # Detect collision with left and right side walls
    if ball.xcor() > 320 or ball.xcor() < -320:
        ball.bounce_x()
    # Detect collision with paddle
    if (
        abs(ball.xcor() - paddle.xcor()) < 50 and
        abs(ball.ycor() - paddle.ycor()) < 20 and
        ball.y_move < 0  # Only bounce if ball is moving downward
    ):
        ball.redirect_from_paddle(paddle)

    # Detect collision with blocks
    for block in blocks[:]:
        if ball.distance(block) < 40:
            blocks.remove(block)
            block.hideturtle()
            block.goto(1000, 1000)
            counter += 1
            if counter % 2 == 0:
                time_sleep *= 0.91
            ball.bounce_y()
            break


screen.exitonclick()