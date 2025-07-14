from turtle import Turtle

class Block(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1.35, stretch_len=3.2)
        self.shape(color)
        self.goto(position)