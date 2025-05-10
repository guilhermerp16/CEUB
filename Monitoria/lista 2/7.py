lista = input("Digite uma lista de números separados por espaço: ").split()
maior = 0
for i in lista:
    if int(i) > maior:
        maior = int(i)
print(f"O maior número é: {maior}")