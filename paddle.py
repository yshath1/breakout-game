from turtle import Turtle

MOVE_DISTANCE = 10


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def left_(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def right_(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

