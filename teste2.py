num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end="")  # amarelo (divisor)
        tot += 1
    else:
        print('\033[31m', end="")  # vermelho (não divisor)
    print(f"{c}", end=" ")

print('\033[m')  # resetar cor depois do laço

print(f'\nOs números \033[33mamarelos\033[m são divisíveis por {num}')
print(f'O número {num} foi divisível {tot} vezes')

if tot == 2:
    print('\033[32mÉ por isso que ele É PRIMO!\033[m')
else:
    print('\033[31mPor isso ele NÃO é primo!\033[m')
