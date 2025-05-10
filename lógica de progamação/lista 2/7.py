
primeiro = int(input("Digite um número inteiro: "))
for i in range(1, 11):
    resultado = primeiro * i
    print(f"{primeiro:3d} x {i:3d} = {resultado:3d}")

primeiro = int(input("Digite um número inteiro: "))
contador = 1
resultado = 0
while contador <= 10:
    resultado = primeiro * contador
    print(f"{primeiro:3d} x {contador:3d} = {resultado:3d}")
    contador += 1