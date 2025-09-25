from datetime import date
atual = date.today().year
maiores = []
menores = []

for i in range(1, 8):
    nome = str(input(f'Digite o nome da {i}ª pessoa: ')).upper()
    idade = int(input(f'Digite a idade de {nome}: '))
    anoNasc = atual - idade
    
    if idade >= 18:
        maiores.append(nome)
    else:
        menores.append(nome)

print(f'\n\033[31m{len(maiores)} pessoas já atingiram a maioridade.\033[m')
print(f'\033[33m{len(menores)} pessoas ainda NÃO atingiram a maioridade.\033[m')

print(f'\nPessoas MAIORES de idade: {", ".join(maiores)}')
print(f'Pessoas MENORES de idade: {", ".join(menores)}')
