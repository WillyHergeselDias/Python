import turtle
import time
F = turtle.getscreen()
P = turtle.Turtle()
P.clear()
P.shape("square")
turtle.title("Teste")
x=input("Informe uma figura:")
if x == "Circulo" or x =="circulo" or x =="CIRCULO":
    P.shape("circle")
    P.circle(100)
if x == "Quadrado" or x =="quadrado" or x =="QUADRADO":
    P.shape("square")
    x = P.xcor()
    x += 100
    x = P.setx(x)
    time.sleep(0.1)
    x = P.xcor()
    x -= 200
    x = P.setx(x)
    time.sleep(0.1)
    y = P.ycor()
    y += 200
    y = P.sety(y)
    time.sleep(0.1)
    x = P.xcor()
    x += 200
    x = P.setx(x)
    time.sleep(0.1)
    y = P.ycor()
    y -= 200
    y = P.sety(y)
    time.sleep(0.1)
    x = P.xcor()
    x = 0
    x = P.setx(x)
z = input("Deseja apagar a figura atual?(S/N):")
if z == "S":
    P.clear()
y = input("Deseja desenhar outra figura?(S/N):")
while y == "S":
    import turtle
    import time
    F = turtle.getscreen()
    P = turtle.Turtle()
    P.clear()
    P.shape("square")
    turtle.title("Teste")
    x=input("Informe uma figura:")
    if x == "Circulo" or x =="circulo" or x =="CIRCULO":
        P.shape("circle")
        P.circle(100)
    if x == "Quadrado" or x =="quadrado" or x =="QUADRADO":
        P.shape("square")
        x = P.xcor()
        x += 100
        x = P.setx(x)
        time.sleep(0.1)
        x = P.xcor()
        x -= 200
        x = P.setx(x)
        time.sleep(0.1)
        y = P.ycor()
        y += 200
        y = P.sety(y)
        time.sleep(0.1)
        x = P.xcor()
        x += 200
        x = P.setx(x)
        time.sleep(0.1)
        y = P.ycor()
        y -= 200
        y = P.sety(y)
        time.sleep(0.1)
        x = P.xcor()
        x = 0
        x = P.setx(x)
    z = input("Deseja apagar a figura atual?(S/N):")
    if z == "S":
     P.clear()
    y = input("Deseja desenhar outra figura?(S/N):")
