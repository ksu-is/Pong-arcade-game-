#Pong

import turtle

screen = turtle.Screen()
screen.title("Flashback Pong")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)

# Score
#score_a = 0
score_b = 0

# Paddle A
# paddle_a = turtle.Turtle()
# paddle_a.speed(0)
# paddle_a.shape("square")
# paddle_a.color("blue") #changed paddle A to blue
# paddle_a.shapesize(stretch_wid=5,stretch_len=1)
# paddle_a.penup()
# paddle_a.goto(-350, 0) #paddle A location

# Paddle B (The paddle we are changing to the bottom of screen)
paddle_b = turtle.Turtle()
paddle_b.speed(0) #paddle speed 
paddle_b.shape("square")
paddle_b.color("red") #changed paddle B to red
paddle_b.shapesize(stretch_wid=1,stretch_len=5)
paddle_b.penup()
paddle_b.goto(0, -200) #location of paddle B

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black") #changed ball color to black
ball.penup()
ball.goto(0, 200)
ball.dx = 3.5
ball.dy = 3.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}".format(score_b), align="center", font=("Courier", 24, "normal")) #code for title and scoreboard

# Function
# def paddle_a_up():
#     y = paddle_a.ycor()
#     y += 20
#     paddle_a.sety(y)

# def paddle_a_down():
#     y = paddle_a.ycor()
#     y -= 20
#     paddle_a.sety(y)

# def paddle_b_up():
#   y = paddle_b.ycor()
#   y += 20
#   paddle_b.sety(y)

# def paddle_b_down):
#    y = paddle_b.ycor()
#    y -= 20
#    paddle_b.sety(y)

def paddle_b_left():
    x = paddle_b.xcor()
    x += -30
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 30
    paddle_b.setx(x)


# Keyboard binding
screen.listen()
#screen.onkeypress(paddle_a_up, "w")
#screen.onkeypress(paddle_a_down, "s")
#screen.onkeypress(paddle_b_up, "Up")
#screen.onkeypress(paddle_b_down, "Down")

screen.onkeypress(paddle_b_left, "Left")
screen.onkeypress(paddle_b_right, "Right")

# Main game loop
while True:
    screen.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
            
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dx *= -1
    
    #new code for ball to bounce off side walls
    elif ball.xcor() > 400:
        ball.setx(400)
        ball.dx *= -1

    elif ball.xcor() < -400:
        ball.setx(-400)
        ball.dx *= -1

    # Left and right
    # if ball.xcor() > 350:
    #     score_a += 1
    #     pen.clear()
    #     pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #     ball.goto(0, 0)
    #     ball.dx *= -1

    # elif ball.xcor() < -350:
    #     score_b += 1
    #     pen.clear()
    #     pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #     ball.goto(0, 0)
    #     ball.dx *= -1

    if ball.ycor() <- 250:
        score_b += 1
        pen.clear()
        pen.write("Score: {}".format(score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

      # Paddle and ball collisions
    # if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
    #     ball.dx *= -1 
            
    # elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
    #     ball.dx *= -1
    
    #Paddle and ball collisions for paddle B
        #if ball.ycor() < -180 and ball.xcor() < paddle_b.xcor() + 50 and ball.xcor() > paddle_b.xcor() - 50:
         #
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 50 and ball.xcor() > paddle_b.xcor() - 50:
        ball.sety(-190)
        ball.dy *= 1
