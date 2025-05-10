lista = input("Digite uma lista de números separados por espaço: ").split()
pares = 0 
impares = 0
for i in lista:
    if int(i) % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Essa lista tem {pares} números pares e {impares} números ímpares")