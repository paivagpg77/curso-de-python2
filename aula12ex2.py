#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

primeiro = int(input("Digite um número: "))
segundo = int(input("Digite o segundo número: "))

if primeiro > segundo:
    print("O PRIMEIRO número é MAIOR!")
elif primeiro < segundo:
    print("O SEGUNDO número é MAIOR!")
else: 
    print("Os números são iguais. ")