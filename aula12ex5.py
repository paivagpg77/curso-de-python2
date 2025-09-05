##Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

import datetime 
anonsc = int(input("Digite o seu ano de nascimento:     "))
anoat = datetime.date.today().year

idade = anoat - anonsc

 if idade <= 14:
    print("Você faz parte da categoria INFANTIL")
    print(f"Pois tem {idade} ANOS")

elif idade <= 19 :
    print("Você faz parte da categoria JÚNIOR")
    print(f"Pois tem {idade} ANOS")

elif idade <= 25:
    print("Você faz parte da categoria SÊNIOR") 
    print(f"Pois tem {idade} ANOS")
    
else:
    print("Você faz parte da categoria MASTER")
    print(f"Pois tem {idade} ANOS")