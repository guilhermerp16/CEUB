n = int(input("Digite um número inteiro não negativo: "))
fatorial = 1 
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}.")