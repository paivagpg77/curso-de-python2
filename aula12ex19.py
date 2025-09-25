#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
idades = []
nomes = []
sexos = []
for p in range(1,5):
    print(f'----{p}º Pessoa----')
    nome = str(input("Digite seu nome: ")).upper()
    idade = int(input(f"Digite a sua idade {nome}: "))
    sexo = input(f"Qual seu sexos? [M/F]: ").upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    média = sum(idades) / len(idades)
maiorIdadeM = -1
nomeMvelho = ' '

for i in range(len(nomes)):
    if sexos[i] == "M" and idades[i] > maiorIdadeM:
        maiorIdadeM = idades[i]
        nomeMvelho = nomes[i]

cont_mulheresMenor20 = 0
for i in range(len(nomes)):
    if sexos[i] == "F" and idades[i] <  20 :
        cont_mulheresMenor20 += 1

print(f'A média de idade do grupo é {média}')
print(f'O {nomeMvelho} é o homem mais velho com {maiorIdadeM} ANOS')                   
print(f'E tem {cont_mulheresMenor20} mulheres maior de idade')