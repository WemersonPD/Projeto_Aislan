from turtle import *
from cores import *
import os
from escolha_player import escolha_player
from desenha_opcoes import desenhar_opcoes
from escolha_nome import escolha_nome
from  cabecalho import cabecalho
from time import sleep
cores = ['red', 'purple', 'blue', 'green']





def jogar():
    os.system("cls" if os.name == "nt" else "clear")
    
    #PARA O PRIMEIRO PLAYER
    cabecalho()
    jogador1 = escolha_nome()
    desenhar_opcoes()
    cor_player1 = escolha_player()
    sleep(1.5)
    clear()
    pencolor('red')
    goto(0,0)
    write('PRIMEIRO PLAYER OK!', align='Center', font=('Arial',30))
    pencolor('black')
    sleep(1.5)
    clear()


    #PARA O SEGUNDO PLAYER
    cabecalho()
    jogador2 = escolha_nome()
    desenhar_opcoes()
    cor_player2 = escolha_player()
    sleep(1.5)
    clear()
    pencolor('red')
    goto(0,0)
    write('SEGUNDO PLAYER OK!', align='Center', font=('Arial',30))
    pencolor('black')
    sleep(1.5)
    clear()
    

    done()

