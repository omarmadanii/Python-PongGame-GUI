from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
from scoreboard_pong import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))


ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(rightPaddle.down, 'Down')
screen.onkey(rightPaddle.up, 'Up')
screen.onkey(leftPaddle.down, 's')
screen.onkey(leftPaddle.up, 'w')


gameOn = True
while gameOn:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # detect collision...
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle...
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

