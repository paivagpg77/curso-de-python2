#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
maiores = []
menores = []

for i in range(1,8):
    nome = str(input('Digite seu nome: ')).upper()
    anoNasc= int(input(f'Digite o ano em que você nasceu {nome}: '))
    idade = atual - anoNasc
    print(idade)
    if idade >= 18:
        maiores.append(nome)
    else:
        menores.append(nome)
print(f'\n\033[31m{len(maiores)} pessoas já atingiram a maioridade.\033[m')
print(f'\033[33m {len(menores)} pessoas ainda NÃO atingiram a maioridade.\033[m')


print(f'As pessoas maior de idade são: {",".join(maiores)}')
print(f'AS pessoas menores de idade são: {",".join(menores)}')
