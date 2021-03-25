from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up, "a")
screen.onkeypress(l_paddle.go_down, "z")

screen.onkeypress(r_paddle.go_up, "o")
screen.onkeypress(r_paddle.go_down, "l")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
        ball.speed_up()

    # Detect miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

    # Detect end of game
    if scoreboard.r_score == 5:
        scoreboard.winner("Right Player")
        game_is_on = False

    if scoreboard.l_score == 5:
        scoreboard.winner("Left Player")
        game_is_on = False

screen.exitonclick()
