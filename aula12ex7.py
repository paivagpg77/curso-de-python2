"""Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros"""
print("========= LOJAS PAIVA ==========") 
precocmp = float(input("Digite o preço das suas compras?: R$"))
print('''FORMAS DE PAGAMENTO
[1] á vista Dinheiro/Cheque
[2] á vista no Cartão 
[3] 2x no Cartão 
[4] 3x ou mais no Cartão''')
opcão = int(input("Qual é a opcão?:  "))
if opcão == 1 :
    total = precocmp - (precocmp*0.10)
    print("Você escolheu a opção 1")
    print("O seu desconto foi de 10%")
    print(f"O produto que era {precocmp} , ficou  por {total}")
elif opcão == 2:
    total = precocmp - (precocmp*0.05)
    print("Você escolheu a opção 2")
    print("O seu desconto foi de 5%")
    print(f"O produto que era {precocmp} , ficou  por {total}")
elif opcão ==3:
    parcela = precocmp /2
    print("Você escolheu a opção 3")
    print(f"Vão ficar 2 parcelas de {parcela:.2f}")
elif opcão == 4:
    totalp = precocmp + (precocmp*0.20)
    parcelas = int(input("Em quantas parcelas você quer: "))
    valor_parcela = totalp /parcelas
    print(f"O valor total com juros é: R${totalp:.2f}")
    print(f"Serão {parcelas}x de R${valor_parcela}")