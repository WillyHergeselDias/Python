import turtle
import time
Fundo = turtle.getscreen()
C = turtle.Screen()
B = turtle.Turtle()
A = turtle.Turtle()
V = turtle.Turtle()
T = turtle.Turtle()
turtle.bgcolor("Black")
turtle.title("Quadrantes Universalises")
B.shape("square")
B.shapesize(1,1)
B.color("White")
B.speed(10)
B.pendown()
B.pencolor("White")
#Definiçao das funçoes do jogador
def jump():
    time.sleep(0.10)
    y = B.ycor()
    y += 15
    y = B.sety(y)
    time.sleep(0.10)
    y = B.ycor()
    y -= 15
    y = B.sety(y)
def right():
    x = B.xcor()
    x += 5
    x = B.setx(x)
def left():
    x = B.xcor()
    x -= 5
    x = B.setx(x)
def alt():
    B.shape("circle")
    B.color("Black")
    turtle.bgcolor("White")
def alt2():
    B.shape("square")
    B.color("White")
    turtle.bgcolor("Black")
#Primeiro Filho
def FirstSon():
    x = A.xcor()
    x = B.xcor()
    x = A.setx(x)
    A.shape("triangle")
    A.shapesize(0.5,0.5)
    A.color("grey")
    A.speed(5)
#Segundo Filho
def SecondSon():
    x = V.xcor()
    x = B.xcor()
    x = V.setx(x)
    V.shape("triangle")
    V.shapesize(0.5,0.5)
    V.color("grey")
    V.speed(5)
#Terceiro Filho
def ThirdSon():
    x = T.xcor()
    x = B.xcor()
    x = T.setx(x)
    T.shape("triangle")
    T.shapesize(0.5,0.5)
    T.color("grey")
    T.speed(5)
#Definição de função para todos os filhos
def sonR():
    x = A.xcor()
    x += 5
    x = A.setx(x)
    
    x = V.xcor()
    x += 5
    x = V.setx(x)
    
    x = T.xcor()
    x += 5
    x = T.setx(x)
def sonL():
    x = A.xcor()
    x -= 5
    x = A.setx(x)
    
    x = V.xcor()
    x -= 5
    x = V.setx(x)
    
    x = T.xcor()
    x -= 5
    x = T.setx(x)
def sonUp():
    y = A.ycor()
    y += 5
    y = A.sety(y)
    
    y = V.ycor()
    y += 5
    y = V.sety(y)
    
    y = T.ycor()
    y += 5
    y = T.sety(y)
def sonDown():
    y = A.ycor()
    y -= 5
    y = A.sety(y)
    
    y = V.ycor()
    y -= 5
    y = V.sety(y)

    y = T.ycor()
    y -= 5
    y = T.sety(y)
def sonPenDown():
    A.pendown()
    V.pendown()
    T.pendown()
def sonPenUp():
    A.penup()
    V.penup()
    T.penup()
def pensizechange():
    PNU = 0
    PNU = PNU + 1
    A.pensize(PNU)
    V.pensize(PNU)
    T.pensize(PNU)
#Conexão entre as funções e as teclas
turtle.listen()
turtle.onkeypress(jump,"space")
turtle.onkeypress(right,"d")
turtle.onkeypress(left,"a")
turtle.onkeypress(alt,"0")
turtle.onkeypress(alt2,"1")
turtle.onkeypress(FirstSon,"2")
turtle.onkeypress(sonR,"Right")
turtle.onkeypress(sonL,"Left")
turtle.onkeypress(sonUp,"Up")
turtle.onkeypress(sonDown,"Down")
turtle.onkeypress(sonPenDown,"o")
turtle.onkeypress(sonPenUp,"l")
turtle.onkeypress(SecondSon,"3")
turtle.onkeypress(ThirdSon,"4")
turtle.onkeypress(pensizechange,"6")
