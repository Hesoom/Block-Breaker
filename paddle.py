from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=5)
        self.shape("img/paddle.gif")
        print(self.shapesize())
        self.penup()
        self.goto(position)
        self.speed = 5

    def move(self, direction):
        new_x = self.xcor() + (self.speed * direction)
        # optional: keep paddle within screen bounds
        if -300 < new_x < 300:
            self.goto(new_x, self.ycor())
