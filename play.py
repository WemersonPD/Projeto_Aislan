from turtle import *
from math import *

#iniciando o jogo
Screen()
bgcolor("black")

#Taxa de atualização do jogo
tracer(3)

#desenhando os limites/bordas do jogo
arena = Turtle()
arena.color("white")
arena.penup()
arena.setposition(-670,-400)
arena.pendown()
arena.pensize(3)
for lado in range(2):
    arena.fd(1320)
    arena.left(90)
    arena.fd(800)
    arena.left(90)
    print(arena.pos())
#arena.hideturtle()
arena.left(90)
arena.fd(400)
arena.right(90)
arena.fd(1320)

#criando o jogador 1
jogador = Turtle()
jogador.color('red')
jogador.shape('triangle')
jogador.penup()
jogador.speed(0)
jogador.goto(-615, 200)


#velocidade
velocidade = 1

# obstaculos
numero_obstaculos = 5
obstaculo_jogador_1 = []
obstaculo_jogador_2 = []

for i in range(numero_obstaculos):
    # obstaculos jogador 1
    obstaculo_jogador_1.append(Turtle())
    obstaculo_jogador_1[i].color("yellow")
    obstaculo_jogador_1[i].shape("circle")

    # obstaculos jogador 2
    obstaculo_jogador_2.append(Turtle())
    obstaculo_jogador_2[i].color("yellow")
    obstaculo_jogador_2[i].shape("circle")

obstaculo_jogador_1[0].setposition(-585, 200)
obstaculo_jogador_1[1].setposition(-500, 40)

# Número de pilulas
numero_pilulas = 2
pilulas_jogador_1 = []
pilulas_jogador_2 = []

# Pilulas de energia
for i in range(numero_pilulas):

    # Para o jogador 1
    pilulas_jogador_1.append(Turtle())
    pilulas_jogador_1[i].color("yellow")
    pilulas_jogador_1[i].shape("circle")
    pilulas_jogador_1[i].penup()
    pilulas_jogador_1[i].speed(0)

    # Para o jogador 2
    pilulas_jogador_2.append(Turtle())
    pilulas_jogador_2[i].color("yellow")
    pilulas_jogador_2[i].shape("circle")
    pilulas_jogador_2[i].penup()
    pilulas_jogador_2[i].speed(0)

# Início das pilulas do jogador 1
pilulas_jogador_1[0].setposition(615, 205)
pilulas_jogador_1[1].setposition(615, 195)

# Início das pilulas do jogador 2
pilulas_jogador_2[0].setposition(615, -205)
pilulas_jogador_2[1].setposition(615, -195)


print(arena.pos())
#ações dos comandos
def vira_a_esquerda():
    jogador.left(30)

def vira_a_direita():
    jogador.right(30)

def frente():
    global velocidade
    velocidade += 0.1

def tras():
    global velocidade
    velocidade -= 0.2

#ações dos comandos
listen()
onkey(vira_a_esquerda,"Left")
onkey(vira_a_direita,"Right")
onkey(frente, "Up")
onkey(tras, 'Down')

#criando o jogador2
jogador2 = Turtle()
jogador2.color('blue')
jogador2.shape('triangle')
jogador2.penup()
jogador2.speed(0)
jogador2.goto(-615, -200)

#velociade jogador 2
velocidade2 = 1

#ações dos comandos
def vira_a_esquerda2():
    jogador2.left(30)

def vira_a_direita2():
    jogador2.right(30)

def aumenta_velocidade2():
    global velocidade2
    velocidade2 += 0.1

def tras2():
    global velocidade2
    velocidade2 -= 0.1

def bateu(objeto1, objeto2):
    distancia = sqrt(pow(objeto1.xcor()-objeto2.xcor(),2)+pow(objeto1.ycor()-objeto2.ycor(),2))
    if distancia < 20:
        return True
    else:
        return False

#comandos do jogo
listen()
onkey(vira_a_esquerda2,"a")
onkey(vira_a_direita2,"d")
onkey(aumenta_velocidade2,"w")
onkey(tras2, 's')

#Principal
while True:
    jogador.forward(velocidade)
    jogador2.forward(velocidade2)

    #verificação de limite/borda jogador 1
    if(jogador.xcor() > 630 or jogador.xcor() < -630):
        jogador.right(180)
    if(jogador.ycor() > 400 or jogador.ycor() < 0):
        jogador.right(180)

    #verificação de limite/borda jogador 2
    if(jogador2.xcor() > 630 or jogador2.xcor() < -630):
        jogador2.right(100)
    if(jogador2.ycor() > 0 or jogador2.ycor() < -400):
        jogador2.right(100)
    
    #movendo as píluas
    for i in range(numero_pilulas):
        pilulas_jogador_1[i].fd(3)
        pilulas_jogador_2[i].fd(3)

        #verificação de limite/borda pilula -> jogador 1
        if pilulas_jogador_1[i].xcor() > 625 or pilulas_jogador_1[i].xcor() < -625:
            pilulas_jogador_1[i].right(100)
        
        if pilulas_jogador_1[i].ycor() > 400 or pilulas_jogador_1[i].ycor() < 0:
            pilulas_jogador_1[i].right(100)
        
        #verificação de limite/borda pilula -> jogador 2
        if pilulas_jogador_2[i].xcor() > 625 or pilulas_jogador_2[i].xcor() < -625:
            pilulas_jogador_2[i].right(100)
        
        if pilulas_jogador_2[i].ycor() > 0 or pilulas_jogador_2[i].ycor() < -400:
            pilulas_jogador_2[i].right(100)
        
        #verificar colisão do jogador 1
        if(bateu(jogador,pilulas_jogador_1[i])):
            jogador.goto(-615, 200)
        
        #verificar colisão do jogador 1
        if(bateu(jogador2,pilulas_jogador_2[i])):
            jogador2.goto(-615, -200)


done()