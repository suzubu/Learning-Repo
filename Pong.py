
#simple pong game 

#set up
import turtle

wn = turtle.Screen()
wn.title("Pong by Suzy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #makes the game move faster, prevents unneccessy update (must manually update)


#score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # default size of items are 20 by 20 pixels; stretch makes its 100 tall by 20 wide
paddle_a.penup()
paddle_a.goto(-350, 0) #coorinated in the "set up"


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #maximum possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # default size of items are 20 by 20 pixels; stretch makes its 100 tall by 20 wide
paddle_b.penup()
paddle_b.goto(350, 0) #coorinated in the "set up"


#Ball
ball = turtle.Turtle()
ball.speed(0) #maximum possible speed
ball.shape("square") # no size parameter added, meaning the item will defaut to 20 by 20 
ball.color("white")
ball.penup()
ball.goto(0, 0) #coorinated in the "set up"
ball.dx = 2 # d = delta
ball.dy = 2 # setting these both to 2 (or the same number) allows for diagonal movement, which will be called upon in the main loop 


# Pen - creating an object for score keeping
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # we dont need to see it 
pen.goto(0,260) #location near the centre/top of the page 
pen.write ("PlayerA: 0  PlayerB: 0", align= "center", font=("Courier", 24, "normal"))


# Functions

#Paddle A Moving Up
def paddle_a_up():
    y = paddle_a.ycor() #from the turtle modul; returns the ycoordinates 
    y += 20
    paddle_a.sety(y)

#Paddle A Moving Down
def paddle_a_down():
    y = paddle_a.ycor() #from the turtle modul; returns the ycoordinates 
    y -= 20
    paddle_a.sety(y)

#Paddle B Moving Up
def paddle_b_up():
    y = paddle_b.ycor() #from the turtle modul; returns the ycoordinates 
    y += 20
    paddle_b.sety(y)

#Paddle A Moving Down
def paddle_b_down():
    y = paddle_b.ycor() #from the turtle modul; returns the ycoordinates 
    y -= 20
    paddle_b.sety(y)

#keyboard binding 
wn.listen() #turtle; tells the program to listen to keyboard input 
wn.onkeypress(paddle_a_up, "w") #when w (lowercase) is pressed call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") #when s(lowercase) is pressed call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") #when up arrow is pressed call the function paddle_b_up
wn.onkeypress(paddle_b_down, "Down") #when down arrow is pressed call the function paddle_b_down

#main game loop

while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx) #at the start, x cor is 0, then 2 will be added to the x cor; this will loop
    ball.sety(ball.ycor() + ball.dy)
    
    #border checking 
    #we want the ball to bounce once it hits a wall; add a score if the other play fails to prevent the ball from going past their paddle  
    
    #top and bottom borders 
    #top
    if ball.ycor() > 290: #box width is 600 (-300 to 300); 290 allows for the ball to appear hit the edge rather than go past it
        ball.sety(290)
        ball.dy *= -1 #reverses direction or "bounce"
    #bottom    
    if ball.ycor() < -290: #box width is 600 (-300 to 300); 290 allows for the ball to appear hit the edge rather than go past it
        ball.sety(-290)
        ball.dy *= -1 #reverses direction or "bounce"
    
    #side borders 
    #right
    if ball.xcor() > 390: #box width is 600 (-400 to 400); 290 allows for the ball to appear hit the edge rather than go past it
        ball.goto(0,0) #goes past the paddle, reset the game / location of the ball
        ball.dx *= -1  #reverses direction or "bounce"
        pen.clear() #clear the displayed score 
        score_a += 1#adds a point 
        pen.write ("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align= "center", font=("Courier", 24, "normal"))
    #left    
    if ball.xcor() < -390: #box width is 600 (-300 to 300); 290 allows for the ball to appear hit the edge rather than go past it
        ball.goto(0,0) #goes past the paddle, reset the game / location of the ball
        ball.dx *= -1 #reverses direction or "bounce"
        pen.clear() #clear the displayed score 
        score_b += 1 #adds a point 
        pen.write ("PlayerA: {}  PlayerB: {}".format(score_a, score_b), align= "center", font=("Courier", 24, "normal"))
        #displays the updated score 

    #paddle and ball collition
    
    #paddle A (left side)        
    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        # the paddle is 20 pixels wide by 100 pixels tall 
        # the centre of the paddle on the x axis is @ 350; the width of the paddle would be 340-360
        # the centre of the paddle on the y axis can change so to collide withthe paddle we can base location of the collision on the changing coordinates of the paddle 
        #if the balls location on the x axis is between coord 340 and 350 (the front halfof the paddle)
        #AND the y coordinates are within the centre of he paddle + or - 40 pixels (size of ball is 20); then it would bounce 
        ball.setx(-340) #keep it on the edge of the paddle 
        ball.dx *= -1 #bounce
    
    
    #paddle B (right side)        
    if (ball.xcor() > 340 and ball.xcor() <350) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        # the paddle is 20 pixels wide by 100 pixels tall 
        # the centre of the paddle on the x axis is @ 350; the width of the paddle would be 340-360
        # the centre of the paddle on the y axis can change so to collide withthe paddle we can base location of the collision on the changing coordinates of the paddle 
        #if the balls location on the x axis is between coord 340 and 350 (the front halfof the paddle)
        #AND the y coordinates are within the centre of he paddle + or - 40 pixels (size of ball is 20); then it would bounce 
        ball.setx(340) #keep it on the edge of the paddle 
        ball.dx *= -1 #bounce