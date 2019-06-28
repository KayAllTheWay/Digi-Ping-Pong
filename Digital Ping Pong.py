import turtle 

win = turtle.Screen()
win.title("Digi Ping Pong by Kenita")
win.bgcolor("White")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a = 0
score_b = 0 
 

#Bat A
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("black")
bat_a.shapesize(stretch_wid=5,  stretch_len=1)
bat_a.penup()
bat_a.goto(-350, 0)
 
#Bat B
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("black")
bat_b.shapesize(stretch_wid=5,  stretch_len=1)
bat_b.penup()
bat_b.goto(+ 350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#Pen
pen = turtle.Turtle( )
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24, "normal"))

#Function
def bat_a_up():
	y = bat_a.ycor()
	y += 20
	bat_a.sety(y)

def bat_a_down():
	y = bat_a.ycor()
	y -= 20
	bat_a.sety(y)


def bat_b_up():
	y = bat_b.ycor()
	y += 20
	bat_b.sety(y)

def bat_b_down():
	y = bat_b.ycor()
	y -= 20
	bat_b.sety(y)

#Keyboard binding
win.listen()  
win.onkeypress(bat_a_up, "q")
win.onkeypress(bat_a_down, "a")	
win.onkeypress(bat_b_up, "Up")
win.onkeypress(bat_b_down, "Down")

# Main game loop
while True:
	win.update() 


	#Move the ball
	ball.setx(ball.xcor() + ball.dx) 
	ball.sety(ball.ycor() + ball.dy) 

	# Border checking
	if ball .ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball .ycor() < -290:  
		ball.sety(-290) 
		ball.dy *= -1


	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		score_a +=1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))


	if ball.xcor() < -390:
		ball.goto(0,0)	
		ball.dx *= -1
		score_b +=1	
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

	#Bat and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <bat_b.ycor() + 50 and ball.ycor() > bat_b.ycor() -50):
		ball.setx(340) 
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <bat_a.ycor() + 50 and ball.ycor() > bat_a.ycor() -50):
		ball.setx(-340) 
		ball.dx *= -1

    
    