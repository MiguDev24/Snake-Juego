import turtle
import time
import random

posponer=0.1

#marcador
score=0
high_score=0
#Parte de la pantalla
screen=turtle.Screen()
screen.title("SNAKE BY NINJA")
screen.bgcolor("black")
screen.setup(width=600,height=600)

#Creacion de la Cabeza de la Serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction ="stop"

#Creacion de la Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,110)

#Cuerpo de la Serpiente
cuerpo = []

#Texto
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0        High Score: 0",align="center", font=("Courier", 24, "normal"))


#Funciones Movimiento
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"

#Mecanicas de Movimiento
def movimiento():
    if cabeza.direction=="up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        x=cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction=="right":
        x=cabeza.xcor()
        cabeza.setx(x+20)

#Teclado para Captar indicaciones
screen.listen()
screen.onkey(arriba,"Up")
screen.onkey(abajo,"Down")
screen.onkey(izquierda,"Left")
screen.onkey(derecha,"Right")
    

while True:
    screen.update()
    
    # colisión entre los bordes = game over
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        for cuerpo_segmento in cuerpo:
            cuerpo_segmento.hideturtle()
        cuerpo.clear()

        score = 0
        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # colisión entre la cabeza y el cuerpo
    for i in range(1, len(cuerpo)):
        if cabeza.distance(cuerpo[i]) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            for cuerpo_segmento in cuerpo:
                cuerpo_segmento.hideturtle()
            cuerpo.clear()

            score = 0
            texto.clear()
            texto.write("Score: {}        High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            break
    
    if cabeza.distance(comida) < 20:  #colisión entre la cabeza y la comida
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("light green")
        nuevo_cuerpo.penup()
        cuerpo.append(nuevo_cuerpo)

        score += 1
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score: {}        High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #Mover el cuerpo de la serpiente
    totalcuerpo = len(cuerpo)
    for index in range(totalcuerpo - 1, 0, -1): #hace que el último cuerpo que se añadió siga al anterior
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)
    if totalcuerpo > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)
    
    movimiento()
    time.sleep(posponer)