positivos = 0
negativos = 0
while True:
    n = float(input("Digite um número inteiro (0 para parar): "))
    if n == 0:
        break
    elif n > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")