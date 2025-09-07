"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input("Qual o seu peso? (kg): "))
altura = float(input("Qual a sua altura? (M): "))
imc = peso/(altura**2)

if imc < 18.5:
    print(f"O seu IMC é {imc:1f}")
    print("Você está ABAIXO DO PESO!!")
elif imc >= 18.5 and imc < 25:
    print(f"O seu IMC é {imc:.1f}")
    print("Você está no peso IDEAL!!")
elif imc >= 25 and imc < 30:
    print(f"O seu IMC é {imc:.1f}")
    print("Você está com SOBREPESO!!")
elif imc >= 30 and imc < 40:
    print(f"O seu IMC é {imc:.1f}") 
    print("Você está em estado de OBESIDADE!!, PROCURE AJUDA!")
else:
    print(f"O seu IMC é {imc:.1f}")
    print("Você está em estado de OBESIDADE MÓRBIDA!!, PROCURE AJUDA!!")