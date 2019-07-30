def participantes(nome_participante):
    todos_os_participantes = open("nick.txt", "a")
    todos_os_participantes.write(nome_participante + "\n")
    todos_os_participantes.close()

def pontuacao(somatoria):
    todos_os_pontos = open("tempo.txt", "a")
    todos_os_pontos.write(str(somatoria) + "\n")
    todos_os_pontos.close()

def ver_participantes():
    pessoa = open('nick.txt', 'r')
    lista_pessoa = []
    for i in pessoa:
        i = i.strip()
        lista_pessoa.append(i)
    pessoa.close()
    return lista_pessoa

def ver_pontuacao():
    ponto = open('tempo.txt', 'r')
    lista_pontuacao = []
    for i in ponto:
        i = i.strip()
        lista_pontuacao.append(float(i))
    ponto.close()
    return lista_pontuacao

def organizar():
    lista_nomes = ver_participantes()
    lista_pontos = ver_pontuacao()

    for i in range(len(lista_pontos)):
        for j in range(len(lista_pontos)):
            if(lista_pontos[i] < lista_pontos[j]):

                aux_pontos = lista_pontos[i]
                lista_pontos[i] = lista_pontos[j]
                lista_pontos[j] = aux_pontos

                aux_nomes = lista_nomes[i]
                lista_nomes[i] = lista_nomes[j]
                lista_nomes[j] = aux_nomes

    if(len(lista_nomes) != 0):
        for l in range(len(lista_pontos)):
            print("{} - {} {}".format(l+1, lista_nomes[l], lista_pontos[l]))
    else:
        print()
        print("***Histórico de partidas inexistente***")