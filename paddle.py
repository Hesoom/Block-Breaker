from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=5)
        self.shape("img/paddle.gif")
        self.penup()
        self.goto(position)

    def move(self, direction):
        step = 10
        new_x = self.xcor() + direction * step
        if -280 < new_x < 280:
            self.goto(new_x, self.ycor())

