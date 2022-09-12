from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_rec = Paddle((350, 0))
l_rec = Paddle((-350, 0))

ball = Ball()

score = Score()

screen.listen()
screen.onkey(r_rec.go_up, "Up")
screen.onkey(r_rec.go_down, "Down")

screen.onkey(l_rec.go_up, "w")
screen.onkey(l_rec.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle
    if ball.xcor() > 320 and ball.distance(r_rec) < 50 or ball.xcor() < -320 and ball.distance(l_rec) < 50:
        ball.bounce_x()

    # Out of border, right side
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # Out of border, left side
    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
