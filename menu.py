from cores import vermelho, amarelo, verde
import os
from ranking import organizar
from time import sleep

os.system("cls" if os.name == "nt" else "clear")
print(amarelo("MENU"))
print(amarelo("1 - JOGAR"))
print(amarelo("2 - RANKING"))
print(amarelo("3 - SAIR"))
request = input(verde("ESCOLHA: "))
while not( request == "1" or request == "2"or request == "3"):
    os.system("cls" if os.name == "nt" else "clear")
    print(vermelho("OPÇÃO INVÁLIDA"))
    print(amarelo("1 - JOGAR"))
    print(amarelo("2 - RANKING"))
    print(amarelo("3 - SAIR"))
    
    request = input(verde("ESCOLHA: "))

    if(request == "3"):
        break

    
while True:
    if(request == "1"):
        import play
    elif(request == "2"):
        organizar()
        opcao_voltar = input(verde("PARA VOLTAR AO MENU INICIAL DIGITE 1: "))
        os.system("cls" if os.name == "nt" else "clear")
        if(opcao_voltar == "1"):
            print(amarelo("1 - JOGAR"))
            print(amarelo("2 - RANKING"))
            print(amarelo("3 - SAIR"))
            request = input(verde("ESCOLHA: "))
            while not( request == "1" or request == "2" or request == "3"):
                os.system("cls" if os.name == "nt" else "clear")
                print(vermelho("OPÇÃO INVÁLIDA"))
                print(amarelo("1 - JOGAR"))
                print(amarelo("2 - RANKING"))
                print(amarelo("3 - SAIR"))
        
                request = input(verde("ESCOLHA: "))
        else:
            while(opcao_voltar != "1"):
                print(vermelho("OPÇÃO INVÁLIDA"))
                opcao_voltar = input(verde("PARA VOLTAR AO MENU INICIAL DIGITE 1: "))
                os.system("cls" if os.name == "nt" else "clear")
            
            print(amarelo("1 - JOGAR"))
            print(amarelo("2 - RANKING"))
            print(amarelo("3 - SAIR"))
            request = input(verde("ESCOLHA: "))
            while not( request == "1" or request == "2" or request == "3"):
                os.system("cls" if os.name == "nt" else "clear")
                print(vermelho("OPÇÃO INVÁLIDA"))
                print(amarelo("1 - JOGAR"))
                print(amarelo("2 - RANKING"))
                print(amarelo("3 - SAIR"))
        
                request = input(verde("ESCOLHA: "))
        

    elif(request == "3"):
        break