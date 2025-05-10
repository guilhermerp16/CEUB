razão = int(input("Digite a razão da PA: "))
qtermo = int(input("Digite o quarto termo da PA: "))
quantidade = int(input("Digite ate qual termo deseja somar?: "))
primeiro_termo = qtermo - 3 * razão
contador = 1
resultado = primeiro_termo
print(f"O {contador}º termo é: {primeiro_termo:4d}")
while contador < quantidade:
    resultado += razão
    contador += 1
    print(f"O {contador}º termo é: {resultado:4d}")
print (f"A soma dos termos é: {(resultado+primeiro_termo)*(contador)/2}")