from turtle import *

cores = ['red', 'purple', 'blue', 'green']
def escolha_player():
    player_atual = Turtle()
    
    #Deixando a turtle invisivel por enquanto
    player_atual.hideturtle()

    pencolor('white')
    

    cor_player = textinput('COR DO PLAYER', '(1 - VERMELHO, 2 - ROSA, 3 - AZUL, 4 - VERDE) ')
    while not(cor_player == '1' or cor_player == '2'  or cor_player == '3' or cor_player == '4'):
        cor_player = textinput('OPÇÃO INVALIDA!', '(1 - VERMELHO, 2 - ROSA, 3 - AZUL, 4 - VERDE) ')
    
    

    #escolha da cor
    cor_player = int(cor_player) - 1
    
    
    return cor_player