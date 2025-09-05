#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

m1 = float(input("Digite sua primeira nota: "))
m2 = float(input("Digite sua segunda nota:  "))
mf = (m1+m2)/2
if mf < 5.0:
    print(f"Sua média foi {mf}")
    print("VOCÊ ESTÁ REPROVADO!")
elif mf >=5 and mf <7:
    print(f"Sua média foi {mf}")
    print("Você está de RECUPERAÇÃO!")
else:
    print(f"Sua média foi {mf}")
    print("VOCÊ ESTÁ APROVADO!!!")