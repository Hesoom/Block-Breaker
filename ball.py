from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = -1
        self.y_move = 2
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def redirect_from_paddle(self, paddle):
        """
        Change x_move and y_move based on where the ball hits the paddle.

        1. Offset = ball.x - paddle.x, normalised to –1 … 1
        2. Steeper angles near the edges, flatter near the centre
        """
        # width/2 in pixels; adjust if you changed shapesize
        half_width = paddle.shapesize()[1] * 10  
        offset = (self.xcor() - paddle.xcor()) / half_width  # -1 (left) … +1 (right)

        # pick a fixed overall speed so the ball doesn’t slow down
        speed = (self.x_move**2 + self.y_move**2) ** 0.5

        # choose an angle up to ~60° at the edges
        max_angle = 50  # degrees
        angle = offset * max_angle

        # convert polar back to x/y
        from math import radians, sin, cos
        self.x_move = speed * sin(radians(angle))
        self.y_move = speed * cos(radians(angle))
        # always move upward after a paddle hit
        if self.y_move < 0:
            self.y_move *= -1

    def redirect_from_paddle_simple(self, paddle):
        # Check where the ball is relative to paddle center
        if self.xcor() < paddle.xcor():
            # Ball is on the left half of the paddle
            self.x_move = -abs(self.x_move)  # move left
        else:
            # Ball is on the right half of the paddle
            self.x_move = abs(self.x_move)   # move right

        self.y_move = abs(self.y_move)      