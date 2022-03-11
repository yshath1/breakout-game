from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from foods import CarManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((-10, -260))
ball = Ball()
scoreboard = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(paddle.left_, "Left")
screen.onkey(paddle.right_, "Right")

num = 0
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    cars.create_car()
    # if ball.xcor() > 320 or ball.xcor() < -320:
    #     ball.bounce_x()

    # left wall
    if ball.xcor() > 380:
        ball.bounce_x()
    # right wall
    if ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.xcor() > -280:
        ball.bounce_y()

        # Detect collision with car
    for car in cars.all_cars:
        if car.distance(ball) < 20:
            car.hideturtle()
            num += 1
    if num == 10:
        scoreboard.l_point()
        num = 0
screen.exitonclick()
