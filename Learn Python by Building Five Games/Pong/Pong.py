import turtle # This is used for the graphics

# Setting up the window
win =  turtle.Screen() # This creates the window
win.title("Pong")
win.bgcolor("Black") # Sets the background colour to black 
win.setup(width=800, height=600) # 0 is in the middle, so goes from -400 to 400, and -300 to 300
win.tracer(0) # Stops the windo from updating

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1


# Functions
def paddle_a_up():# Paddle moving up function
    y = paddle_a.ycor() # Gets current y cord
    y += 20 # Adds 20 pixels
    paddle_a.sety(y) # Moves the paddle to the new location

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

# Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update() # Updates the screen everytime the loop is run 
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # This reverses the balls 
        
    if ball.ycor() < - 290:
        ball.sety( - 290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < - 390:
        ball.goto(0, 0)
        ball.dx *= -1

