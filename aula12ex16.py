print('=' * 5, '\033[31mDetector de Palíndromo\033[m', '=' * 5)
frase = str(input('Digite a frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Então a frase é palindrome!')
else:
    print(junto,inverso)
    print('A frase ou palavra NÃO é palindrome')