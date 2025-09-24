#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date
atual = date.today().year
maiores = 0
menores = 0

for i in range(1,8):
    nasc = int(input(f'Digite a idade da {i} pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        maiores+=1
    else:
        menores-=1
print(f'\n\033[31m{maiores} pessoas já atingiram a maioridade.\033[m')
print(f'\033[33m{menores} pessoas ainda NÃO atingiram a maioridade.\033[m')
