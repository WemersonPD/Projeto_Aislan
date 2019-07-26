
from cores import vermelho, amarelo, verde
import os
from jogando import jogar

os.system("cls" if os.name == "nt" else "clear")
print(amarelo("MENU"))
print(amarelo("1 - JOGAR"))
print(amarelo("2 - SAIR"))
request = input(verde("ESCOLHA: "))
while not( request == "1" or request == "2"):
    os.system("cls" if os.name == "nt" else "clear")
    print(vermelho("OPÇÃO INVÁLIDA"))
    print(amarelo("1 - JOGAR"))
    print(amarelo("2 - SAIR"))
    request = input(verde("ESCOLHA: "))

if request == "1":
    jogar()
