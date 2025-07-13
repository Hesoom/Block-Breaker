from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from block import Block
import time


screen = Screen()
screen.bgcolor("#121212")
screen.setup(width=600, height=600)
screen.title("Breakout")
screen.tracer(0)

ball = Ball()
paddle = Paddle((0,-250))

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

# Creating blocks
blocks = []
start_x = -240
start_y = 260
rows = 4
columns = 7
x_spacing = 80
y_spacing = 40
colors = ["#3e51b5","#b53e3e","#b5b13e","#54a644"]
for row in range(rows):
    for col in range(columns):
        x = start_x + col * x_spacing
        y = start_y - row * y_spacing
        color = colors[row]
        block = Block(position=(x, y), color=color)
        blocks.append(block)

game_is_on = True
counter = 0
time_sleep = 0.008

while game_is_on:
    screen.update()
    time.sleep(time_sleep)
    ball.move()

    # Detect collision with upper wall
    if ball.ycor() > 280:
        ball.bounce_y()
    # Detect collision with left and right side walls
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()
    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < - 230:
        ball.bounce_y()

    # Detect collision with blocks
    for block in blocks[:]:
        if ball.distance(block) < 50:
            blocks.remove(block)
            block.hideturtle()
            block.goto(1000, 1000)
            counter += 1
            if counter % 3 == 0:
                time_sleep *= 0.91
                print(time_sleep)
            ball.bounce_y()
            break

screen.exitonclick()