#Faça um programa que peça um número inteiro para o usuário e mostra a tabuada desse número.
numero = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")