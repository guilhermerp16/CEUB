soma = 0
contador = 0
while True:
    numero = int(input("Digite um número inteiro (negativo para sair): "))
    if numero < 0:
        break
    soma += numero
    contador += 1
print(f"A média dos números digitados é: {soma / contador:.2f}" if contador > 0 else "Nenhum número foi digitado.")