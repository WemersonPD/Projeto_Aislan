from turtle import *
from cores import *
import os

'''a = Turtle()
cord = a.pos()
print(cord)
input()'''

cores = ['red', 'purple', 'blue', 'green']

def desenhar():
    Screen()
    
    goto(-60, 0)
    for i in range(len(cores)):
        atual = i + 1
        pencolor(cores[i])
        write(atual, align='center')
        penup()
        rt(90)
        fd(20)
        pendown()
        stamp()
        
        penup()
        back(20)
        lt(90)
        fd(40)
    
    hideturtle()
    
    



def jogar():
    os.system("cls" if os.name == "nt" else "clear")
    
    print(azul('CORRIDA:'))
    print()
    
    jogador1 = input(verde('NOME DO PRIMEIRO JOGADOR: '))
    
    print(amarelo('OLA'), jogador1,  amarelo('ESCOLHA SEU PLAYER: '))
    desenhar()
    input()
