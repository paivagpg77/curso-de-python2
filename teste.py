import datetime

anonsc = int(input("Digite o seu ano de nascimento: "))

anoat = datetime.date.today().year  # ano atual
idade = anoat - anonsc

if idade <= 14:
    print("Você faz parte da categoria INFANTIL")
    print(f"Pois tem {idade} anos")

elif idade <= 19:
    print("Você faz parte da categoria JÚNIOR")
    print(f"Pois tem {idade} anos")

elif idade <= 25:
    print("Você faz parte da categoria SÊNIOR")
    print(f"Pois tem {idade} anos")

else:
    print("Você faz parte da categoria MASTER")
    print(f"Pois tem {idade} anos")