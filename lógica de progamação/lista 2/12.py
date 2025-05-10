razão = int(input("Digite a razão da PA: "))
número_termo = int(input("Digite o número do termo que deseja encontrar: "))
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
contador = 1
resultado = primeiro_termo
print(f"O {contador:02d}º termo é: {primeiro_termo:3d}")
while contador < número_termo:
    resultado += razão
    contador += 1
    print(f"O {contador:02d}º termo é: {resultado:3d}")
print(f"A soma dos termos é: {(resultado+primeiro_termo)*(contador)/2}")