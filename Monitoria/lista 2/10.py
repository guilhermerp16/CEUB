lista = input("Digite uma lista de números separados por espaço: ").split()
contagem = {}
for i in lista:
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1
print("Contagem de elementos na lista:")
for elemento, contagem in contagem.items():
    print(f"{elemento}: {contagem} vezes")