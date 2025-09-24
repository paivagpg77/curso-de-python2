num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=" ")
        tot+=1
    else:
        print('\033[31m', end=" ")
    print(f"{c}" ,end =" ")
print(f'\n\033[mOs números amarelos são os números que são divisíveis por {num}')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot ==2:
    print('É por isso que ele É PRIMO!')
else:
    print('Por isso ele NÃO! é primo')