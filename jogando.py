from turtle import *
from cores import *
import os
from Players.escolha_player import escolha_player
from Players.desenha_opcoes import desenhar_opcoes
from Players.escolha_nome import escolha_nome
from  Players.cabecalho import cabecalho
from time import sleep
import ranking

cores = ['red', 'purple', 'blue', 'green']

def jogar():
    lista = []

    os.system("cls" if os.name == "nt" else "clear")
    
    #PARA O PRIMEIRO PLAYER
    cabecalho()
    jogador1 = escolha_nome()
    desenhar_opcoes()
    cor_player1 = cores[escolha_player()]
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
    cor_player2 = cores[escolha_player()]
    sleep(1.5)
    clear()
    pencolor('red')
    goto(0,0)
    write('SEGUNDO PLAYER OK!', align='Center', font=('Arial',30))
    pencolor('black')
    sleep(1.5)
    clear()

    lista.append(jogador1)
    lista.append(jogador2)
    lista.append(cor_player1)
    lista.append(cor_player2)

    print(lista)

    return lista

    done()