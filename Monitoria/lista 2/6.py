
lista = input("digite números separados por espaço: ").split()
soma = 0
for i in range(len(lista)):
    lista[i] = int(lista[i])
soma = lista[0] + lista[-1]
print("A soma do primeiro e do ultimo elemento é:", soma)