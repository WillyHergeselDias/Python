import turtle
Fundo=turtle.getscreen()
W=turtle.Turtle()
turtle.bgcolor("Black")
turtle.title("Joguinho :D")
W.shape("circle")
W.shapesize(0.5,0.5)
W.color("Grey", "White")
W.speed(3)
W.pensize(10)
W.pencolor("white")
def up():
   y= W.ycor()
   y +=10
   y= W.sety(y) 
def down():
    y= W.ycor()
    y -=10
    y= W.sety(y)
def left():
    x= W.xcor()
    x -=10
    x= W.setx(x)
def right():
    x= W.xcor()
    x +=10
    x = W.setx(x)
def stop():
    W.penup()
def continue2():
    W.pendown()
def dele():
    W.clear()
def red():
   W.color("Red")
def green():
   W.color("Green")
def blue():
   W.color("Blue")
def yellow():
   W.color("Yellow")
turtle.listen()
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.onkeypress(stop,"w")
turtle.onkeypress(continue2,"s")
turtle.onkeypress(dele,"l")
turtle.onkeypress(red,"1")
turtle.onkeypress(green,"2")
turtle.onkeypress(blue,"3")
turtle.onkeypress(yellow,"4")



    

