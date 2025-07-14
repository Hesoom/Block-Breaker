from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from block import Block
from heart import Heart
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
screen.addshape("img/heart.gif")

# Setup pen for writing messages on screen
pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,0)
pen.color("white")

pen.write("Press ↑ to start", align="center", font=("Courier", 18, "bold"))

ball = Ball((0,-220))
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

def reset_blocks():
    global blocks
    for block in blocks:
        block.hideturtle()
        block.goto(1000, 1000)  # Move them offscreen just in case
    blocks = []  # Clear the old list

    for row in range(rows):
        for col in range(columns):
            x = start_x + col * x_spacing
            y = start_y - row * y_spacing
            color = colors[row]
            block = Block(position=(x, y), color=color)
            blocks.append(block)

reset_blocks()

# Display HP
hearts_list = []
hearts = 3
heart_start_x = -280

def reset_hearts():
    global hearts, hearts_list
    for heart in hearts_list:
        heart.hideturtle()
        heart.goto(1000, 1000)
    hearts_list = []

    hearts = 3
    heart_start_x = -280
    for i in range(1, hearts + 1):
        heart = Heart((heart_start_x, 300), "img/heart.gif")
        hearts_list.append(heart)
        heart_start_x += 40

reset_hearts()

# Start Game with UP arrow
game_started = False
def start_game():
    global game_started
    game_started = True
screen.onkeypress(start_game, "Up")

def game_loop():
    global game_started
    if game_started:
        
        pen.clear()
        ball.move()

        if right_pressed:
            paddle.move(direction=1)
        if left_pressed:
            paddle.move(direction=-1)

        # Wall collision
        if ball.ycor() > 320:
            ball.bounce_y()
        if ball.xcor() > 320 or ball.xcor() < -320:
            ball.bounce_x()

        # Paddle collision
        if (
            abs(ball.xcor() - paddle.xcor()) < 50 and
            abs(ball.ycor() - paddle.ycor()) < 20 and
            ball.y_move < 0
        ):
            ball.redirect_from_paddle(paddle)

        # Block collision
        for block in blocks[:]:
            if (
                abs(ball.xcor() - block.xcor()) < 45 and  # 35 block width + 10 ball radius
                abs(ball.ycor() - block.ycor()) < 25      # 15 block height + 10 ball radius
            ):
                blocks.remove(block)
                block.hideturtle()
                block.goto(1000, 1000)
                ball.x_move *= 1.03
                ball.y_move *= 1.03
                ball.bounce_y()
                break
                    
        # Lose
        global hearts, hearts_list          
        if ball.ycor() < -300:
            game_started = False
            ball.reset()
            paddle.reset()

            if hearts > 1:                  
                hearts -= 1
                # remove one heart icon
                lost_heart = hearts_list.pop()  
                lost_heart.hideturtle()
                lost_heart.goto(1000, 1000)
            else:
                pen.write("Game Over!\nPress ↑ to Play again", align="center", font=("Courier", 18, "bold"))
                reset_blocks()
                reset_hearts()

        # Win
        if len(blocks) == 0:
            game_started = False
            ball.reset()
            paddle.reset()
            pen.write("You Won!\nPress ↑ to Play again", align="center", font=("Courier", 18, "bold"))
            reset_blocks()
            reset_hearts()
            


                

    screen.update()
    screen.ontimer(game_loop, 16)  # About 60 FPS

game_loop()

screen.exitonclick()