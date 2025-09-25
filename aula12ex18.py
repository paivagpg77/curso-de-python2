#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []
for i in range(1,6):
    peso = float(input(f"Digite o peso da {i} pessoa (kg): "))
    pesos.append(peso)
print(f'O maior peso que tivemos foi {max(pesos)}KG')
print(f'O menor peso que tivemos foi {min(pesos)}KG')