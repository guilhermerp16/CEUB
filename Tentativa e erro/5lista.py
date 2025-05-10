lista = input("digite sua lista: ").split(",")
lista = [(i) for i in lista]
lista.sort()
for i in range(len(lista)):
    print(f"{i+1} - {lista[i]}")
escolha = int(input("Escolha o número do item que você deseja comprar: "))
if escolha > len(lista):
    print("Item inválido")
elif escolha < 1:
    print("Item inválido")
elif escolha <= len(lista):
    print(f"Você escolheu {lista[escolha-1]}")
