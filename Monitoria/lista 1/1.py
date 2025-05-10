# # Comparação de números
primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
if primeiro > segundo:
    print("O primeiro número é maior que o segundo.")
elif primeiro < segundo:
    print("O primeiro número é menor que o segundo.")
elif primeiro == segundo:
    print("Os números são iguais.")
else:
    print("Operador inválido")