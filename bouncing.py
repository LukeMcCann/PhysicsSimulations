import turtle

window = turtle.Screen()
window.bgcolor("Black")
window.title("Bouncing Ball Sim")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = 0

gravity = 0.1

while True:

    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -300:
        ball.dy *= -1


