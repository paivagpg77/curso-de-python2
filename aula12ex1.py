#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valordcs= float(input("Qual o valor da casa que você deseja comprar?: "))
salario = float(input("Qual o seu salrio?: "))
anodpag = int(input("Quantos anos deseja pagar?: "))
lmt = salario*0.30
prest = valordcs / (anodpag*12)

print(f"Para pagar uma casa de R${valordcs:.2f} em {anodpag} anos a prestação será de {prest:.2f}")
if valordcs < lmt :
    print("Emprestimo ACEITO!") 
else: 
    print("Emprestimo NEGADO!")