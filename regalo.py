from turtle import * #graficar vectores
from math import* #Hacer calculos

speed(0)
bgcolor("black")
goto(0,-40)

for i in range(15):
    for j in range(18):
        color("#ffa216")
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
    circle(40,24)

color("black")
shape("circle")
shapesize(0.5)
fillcolor("#8b4513")
angulo=137.508

aureo=angulo*(pi/180)

for i in range(180):
    r=4*sqrt(i)
    teta=i*aureo
    x=r*cos(teta)
    y=r*sin(teta)
    penup()
    goto(x,y)
    setheading(i*angulo)
    pendown()
    stamp()

done()