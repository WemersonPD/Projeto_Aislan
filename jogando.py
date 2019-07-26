from turtle import *
from cores import *
import os
from escolha_player import escolha_player
from desenha_opcoes import desenhar_opcoes
from escolha_nome import escolha_nome
from  cabecalho import cabecalho
from time import sleep
cores = ['red', 'purple', 'blue', 'green']


def player_completo():
    cabecalho()
    jogador1 = escolha_nome()
    desenhar_opcoes()
    cor_player1 = escolha_player()
    sleep(1.5)
    clear()
    pencolor('red')
    write('PRIMEIRO PLAYER OK!')
    pencolor('black')
    sleep(1.5)
    clear()

def jogar():
    os.system("cls" if os.name == "nt" else "clear")
    
    #PARA O PRIMEIRO PLAYER
    player1 = player_completo



    done()

