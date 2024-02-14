from turtle import * #graficar vectores
from math import* #Hacer calculos

speed(0) #velocidad
bgcolor("black")
goto(0,-40) #mover la posicion del grafico

#petalos:
for i in range(15):
    #un solo petalo y los de adentro de uno solo:
    for j in range(18):
        color("#2A4FE7")#color petalo
        rt(90) #gira el grafico 90grados a la derecha
        circle(150-j*6,90) #dibuja un semicirculo con la primera posicion de radio y la segunda del segmento de arco
        lt(90) #gira el grafico a la izquierda
        circle(150-j*6,90)
        rt(180)
    circle(40,24) #dibuja el circulo pequeño o del medio

color("black")
shape("circle") #graficar la figura
shapesize(0.5) #reducir el tamaño del curculo
fillcolor("#FFFFFF")#color adentro de la flor
angulo=137.508

aureo=angulo*(pi/180) #angulo en radianes

#adentro de la flor:
for i in range(180):
    r=4*sqrt(i) #calcular el radio de la espiral 
    teta=i*aureo #calcular el angulo en radianes
    x=r*cos(teta) #calcular la coordenada x en el espiral
    y=r*sin(teta) #calcular la coordenada y en el espiral
    penup() #levantar la pluma o dejar de pintar
    goto(x,y) #mover la grafica
    setheading(i*angulo) #nueva direccion para la grafica
    pendown() #bajar la pluma para pintar
    stamp() #dejar marca

done() #no cerrar la ventana