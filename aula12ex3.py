from datetime import date 
atual = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = atual  - nasc
print(f"Quem nasceu em {nasc} tem {idade} Anos")
if idade == 18:
    print("Você precisa se alistar IMEDIATAMENTE!!!")
elif idade > 18 :
    saldo = idade - 18
    print("Seu tempo de alistamento ja passou")
    print(f"Pois ja nasceu em {nasc} e ja tem {idade}")
    print(f"Você  deveria ter se alistado há {saldo} Anos")
    ano = atual - saldo
    print(f"O seu alistamento deveria ter sido em {ano}")
elif idade < 18 :
    saldo = 18 - idade
    print("Você não precisa se alistar ainda ")
    print(f"Pois nasceu em {nasc} e ainda tem {idade} Anos")
    print(f"Você deverá se alistar daqui {saldo} Anos")
    ano = atual + saldo
    print(f"O seu alistamento será em {ano}")



















#    print(f"Você deve ser alistar IMEDIATAMENTE!")
    ###print(f'Pois tem {idade} Anos ')