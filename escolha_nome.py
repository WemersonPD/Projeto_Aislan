from turtle import *
def escolha_nome():
    pencolor('black')
    #nome do novo player
    nome = textinput("CORRIDA MALUCA","NOME DO JOGADOR:")
    
    #recebe a posição atual da caneta
    a = pos()
    #Para não sobreescrever em cima de algo, anda pra baixo
    goto(a[0], a[1] - 40)

    write('OLA, '+ nome,font=("Arial",14), align='center')

    return nome