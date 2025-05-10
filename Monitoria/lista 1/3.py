# # IMC
altura =  float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"IMC: {imc:.2f} - Abaixo do peso")
elif imc <= 24.9:
    print(f"IMC: {imc:.2f} - Peso normal")
elif 25 <= imc:
    print(f"IMC: {imc:.2f} - Sobrepeso")
else:
    print("Valor inválido")