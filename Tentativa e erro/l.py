mercado = ["leite", "pão", "queijo", "manteiga"]
print("Lista de compras:")
for i in range(len(mercado)):
    print(f"{i+1} - {mercado[i]}")
escolha = int(input("Escolha o número do item que você deseja comprar: "))
if escolha > len(mercado):
    print("Item inválido")
elif escolha < 1:   
    print("Item inválido")
elif escolha == 1:
    print("Você escolheu leite")
elif escolha == 2:
    print("Você escolheu pão")
elif escolha == 3:
    print("Você escolheu queijo")
elif escolha == 4:
    print("Você escolheu manteiga")
else:
    print("Item inválido")