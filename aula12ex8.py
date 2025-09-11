import random
opcoes = ['pedra' , 'papel' , 'tesousa']

jogador = str(input("Escolha a sua jogada: ")).lower()
computador = random.choice(opcoes)
print(f'O computador escolheu {computador}')
if jogador == computador:
    print("EMPATE!") 
elif jogador ==  'pedra':
    if computador == "tesoura":
        print("Você Ganhou!")
    else:
        print("Você Perdeu!")
elif jogador == 'papel':
    if computador == 'pedra':
        print('Você Ganhou!')
    else:
        print("Você Perdeu!")
elif jogador  ==  'tesoura':
    if computador ==  'papel':
         print('Você Ganhou!')
    else:
          print("Você Perdeu!")
else:
    print("Valor inválido! escolha Pedra ,Papel ou Tesoura.")