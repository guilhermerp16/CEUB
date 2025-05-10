primeiro = int(input("Digite o primeiro número inteiro positivo: "))
segundo = int(input("Digite o segundo número inteiro positivo: "))
contador = 0
resultado = 1
while primeiro < 0 or segundo < 0:
    print("Os números devem ser inteiros positivos.")
    primeiro = int(input("Digite o primeiro número inteiro positivo: "))
    contador = int(input("Digite o segundo número inteiro positivo: "))
while contador < segundo:
    resultado *= primeiro
    contador += 1
print(f"{primeiro} elevado a {segundo} é igual a {resultado}")