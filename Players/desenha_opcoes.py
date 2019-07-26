from turtle import *
cores = ['red', 'purple', 'blue', 'green']

def desenhar_opcoes():
    Screen()

    #recebe a posição atual da caneta
    a = pos()
    #Para não sobreescrever em cima de algo, anda pra baixo
    goto(a[0], a[1] - 40)
    write('ESCOLHA SEU PERSONAGEM: ', font=('Arial', 14), align='center')

    #recebe a posição atual da caneta
    a = pos()
    #Para não sobreescrever em cima de algo, anda pra baixo
    goto(a[0] - 65, a[1] - 40)

    penup()

    #desenhando as opções:
    for i in range(len(cores)):
        atual = i + 1
        color(cores[i])
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