from turtle import * #Graficos vectores
from colorsys import * #colores y convertidor de colores

bgcolor("black")
tracer(2) #Frecuencia de dibujo
pensize(2) #Grosor de dibujo

h=0

for i in range(210):
    c=hsv_to_rgb(h,1,1)  #Convierte un color en el espacio de color HSV a RGB
    h+=0.005 
    color(c) #Cambiar el color
    up() #dejar de pintar
    goto(-8,25) #Mover la posicion del grafico
    down() #empezar a pintar la nueva grafica
    forward(i) #mueve la grafica un pixel mas
    right(89) #girar la grafica 89grados
    fillcolor(c) #establecer el color de la pluma
    begin_fill() #rellenar la grafica
    circle(90,100) #dibuja el circulo con un radio de 90 píxeles y 100 segmentos de arco
    end_fill() #termina el relleno
    left(179) #girar la grafica 179grados izquierda
    back(i/2) #mover la grafica atras i/2 sin hacer lineas
    left(6) #girar la grafica 6 grados izquierda

done() #mantener la ventana abierta hasta cerrarla