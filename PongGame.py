import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Harashi,@Kasamakii")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

print ("first enter your usernames:")
a = input()
b = input()



# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.40
ball.dy = -0.40

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("magenta")
pen.penup()

pen.hideturtle()
pen.goto(0, 260)
pen.setpos(0,200)
pen.write(" "+a+": 0 ", align="center", font=("Times", 30, "bold italic"))
pen.setpos(0,150)
pen.write(" "+b+": 0 ", align="center", font=("Times", 30, "bold italic"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "8")
wn.onkeypress(paddle_b_down, "5")

# Main game loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.Beep(200, 200), winsound.SND_ASYNC
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.Beep(200, 200), winsound.SND_ASYNC
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.setpos(0,200)
        pen.write(" "+a+": {} ".format(score_a), align="center", font=("Times", 30, "bold italic"))
        pen.setpos(0,150)
        pen.write(" "+b+": {} ".format(score_b), align="center", font=("Times", 30, "bold italic"))
        winsound.Beep(200, 200), winsound.SND_ASYNC
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.setpos(0,200)
        pen.write(" "+a+": {} ".format(score_a), align="center", font=("Times", 30, "bold italic"))
        pen.setpos(0,150)
        pen.write(" "+b+": {} ".format(score_b), align="center", font=("Times", 30, "bold italic"))
        winsound.Beep(200, 200), winsound.SND_ASYNC
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.Beep(500, 500), winsound.SND_ASYNC
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.Beep(500, 500), winsound.SND_ASYNC
