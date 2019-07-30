from turtle import *
from math import *
import time
import ranking
from jogando import jogar

#iniciando o jogo
Screen()
bgcolor("black")

# Configurações do player
config_player = jogar()

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
#arena.hideturtle()
arena.left(90)
arena.fd(400)
arena.right(90)
arena.fd(1320)

#criando o jogador 1
jogador = Turtle()
jogador.color(config_player[2])
jogador.shape('turtle')
jogador.penup()
jogador.speed(0)
jogador.goto(-615, 200)

#velocidade
velocidade = 2

# obstaculos
numero_obstaculos = 6
obstaculo_jogador_1 = []
obstaculo_jogador_2 = []

for i in range(numero_obstaculos):
    # obstaculos jogador 1
    obstaculo_jogador_1.append(Turtle())
    obstaculo_jogador_1[i].color("#FF4500")
    obstaculo_jogador_1[i].shape("circle")
    obstaculo_jogador_1[i].shapesize(stretch_wid = 5, stretch_len = 5)
    obstaculo_jogador_1[i].penup()

    # obstaculos jogador 2
    obstaculo_jogador_2.append(Turtle())
    obstaculo_jogador_2[i].color("#FF4500")
    obstaculo_jogador_2[i].shape("circle")
    obstaculo_jogador_2[i].shapesize(stretch_wid = 5, stretch_len = 5)
    obstaculo_jogador_2[i].penup()

# Locais dos obstaculos do jogador 1
obstaculo_jogador_1[0].setposition(-400, 200)
obstaculo_jogador_1[1].setposition(-250, 350)
obstaculo_jogador_1[2].setposition(-250, 50)
obstaculo_jogador_1[3].setposition(150, 200)
obstaculo_jogador_1[4].setposition(350, 350)
obstaculo_jogador_1[5].setposition(350, 50)

# Locais dos obstaculos do jogador 2
obstaculo_jogador_2[0].setposition(-400, -200)
obstaculo_jogador_2[1].setposition(-250, -350)
obstaculo_jogador_2[2].setposition(-250, -50)
obstaculo_jogador_2[3].setposition(150, -200)
obstaculo_jogador_2[4].setposition(350, -350)
obstaculo_jogador_2[5].setposition(350, -50)

# Ganhou
ganhou = []# Índice 0 == jogador 1 || Índice 1 == jogador 2
for i in range(2):
    ganhou.append(Turtle())
    ganhou[i].color('#800000')
    ganhou[i].shape('circle')
    ganhou[i].penup()
    ganhou[i].speed(0)

ganhou[0].goto(615, 200)
ganhou[0].left(90)
ganhou[1].goto(615, -200)
ganhou[1].left(90)

# Número de pilulas
numero_pilulas = 6
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
pilulas_jogador_1[2].setposition(615, 105)
pilulas_jogador_1[3].setposition(505, 155)
pilulas_jogador_1[4].setposition(550, 100)
pilulas_jogador_1[5].setposition(490, 195)

# Início das pilulas do jogador 2
pilulas_jogador_2[0].setposition(615, -205)
pilulas_jogador_2[1].setposition(615, -195)
pilulas_jogador_2[2].setposition(615, -105)
pilulas_jogador_2[3].setposition(505, -155)
pilulas_jogador_2[4].setposition(550, -100)
pilulas_jogador_2[5].setposition(490, -195)

print(arena.pos())
#ações dos comandos
def vira_a_esquerda():
    jogador.left(30)

def vira_a_direita():
    jogador.right(30)

def frente():
    global velocidade
    velocidade += 0.5

def tras():
    global velocidade
    velocidade -= 0.5

#ações dos comandos
listen()
onkey(vira_a_esquerda,"Left")
onkey(vira_a_direita,"Right")
onkey(frente, "Up")
onkey(tras, 'Down')

#criando o jogador2
jogador2 = Turtle()
jogador2.color(config_player[3])
jogador2.shape('turtle')
jogador2.penup()
jogador2.speed(0)
jogador2.goto(-615, -200)

#velociade jogador 2
velocidade2 = 2

#ações dos comandos
def vira_a_esquerda2():
    jogador2.left(30)

def vira_a_direita2():
    jogador2.right(30)

def aumenta_velocidade2():
    global velocidade2
    velocidade2 += 0.5

def tras2():
    global velocidade2
    velocidade2 -= 0.5

def bateu(objeto1, objeto2):
    distancia = sqrt(pow(objeto1.xcor()-objeto2.xcor(),2)+pow(objeto1.ycor()-objeto2.ycor(),2))
    if distancia < 20:
        return True
    else:
        return False

def bateu_obstaculo(objeto1, objeto2):
    distancia = sqrt(pow(objeto1.xcor()-objeto2.xcor(),2)+pow(objeto1.ycor()-objeto2.ycor(),2))
    if distancia < 60:
        return True
    else:
        return False

#comandos do jogo
listen()
onkey(vira_a_esquerda2,"a")
onkey(vira_a_direita2,"d")
onkey(aumenta_velocidade2,"w")
onkey(tras2, 's')

inicio = time.time()

#Principal
while True:
    jogador.forward(velocidade)
    jogador2.forward(velocidade2)

    ganhou[0].forward(8)
    ganhou[1].forward(8)

    for i in range(numero_pilulas):
        pilulas_jogador_1[i].forward(6)
        pilulas_jogador_2[i].forward(6)

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
        
        #verificar colisão do jogador 1 com as píluas
        if(bateu(jogador,pilulas_jogador_1[i])):
            jogador.goto(-615, 200)
        
        #verificar colisão do jogador 2 com as píluas
        if(bateu(jogador2,pilulas_jogador_2[i])):
            jogador2.goto(-615, -200)
    
    #verificar colisão dos jogadores com os obstaculos
    for i in range(numero_obstaculos):
        # Jogador 1
        if(bateu_obstaculo(jogador,obstaculo_jogador_1[i])):
            jogador.goto(-615, 200)
        
        # Jogador 2
        if(bateu_obstaculo(jogador2,obstaculo_jogador_2[i])):
            jogador2.goto(-615, -200)
        
    #verificar colisão das pílulas com os obstaculos
    for i in range(numero_pilulas):
        for j in range(numero_obstaculos):
            # Pílulas do jogador 1
            if(bateu_obstaculo(pilulas_jogador_1[i],obstaculo_jogador_1[j])):
                pilulas_jogador_1[i].right(90)
            # Pílulas do jogador 2
            if(bateu_obstaculo(pilulas_jogador_2[i],obstaculo_jogador_2[j])):
                pilulas_jogador_2[i].left(90)

    # Verificação de limite/borda ganhou -> jogador 1
    if(ganhou[0].ycor() > 394 or ganhou[0].ycor() < 6):
        ganhou[0].right(180)
    
    # Verificação de limite/borda ganhou -> jogador 2
    if(ganhou[1].ycor() > -6 or ganhou[1].ycor() < -394):
        ganhou[1].right(180)
    
    # Verificar ganhou do jogador 1
    if(bateu(jogador, ganhou[0])):
        vencedor = True
        print("O JOGADOR 1 GANHOU!!!!!")
        break
    
    # Verificar ganhou do jogador 1
    if(bateu(jogador2, ganhou[1])):
        vencedor = False
        print("O JOGADOR 2 GANHOU!!!!!")
        break

fim = time.time()
pontos = fim - inicio

if(vencedor):# Se o jogador 1 ganhar
    ranking.participantes(config_player[0])
else:# Se o jogador 2 ganhar
    ranking.participantes(config_player[1])

ranking.pontuacao(pontos)

done()