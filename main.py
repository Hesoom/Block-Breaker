from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
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

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.009)
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


screen.exitonclick()