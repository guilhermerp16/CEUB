num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    minimo = num1
    maximo = num2
else:
    minimo = num2
    maximo = num1
while True:
    if minimo % num1 == 0 and minimo % num2 == 0:
        break
    minimo += 1
print(f"O mínimo múltiplo comum (MMC) é: {minimo}")
while True:
    if num1 % maximo == 0 and num2 % maximo == 0:
        break
    maximo -= 1
print(f"O máximo divisor comum (MDC) é: {maximo}")