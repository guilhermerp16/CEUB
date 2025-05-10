# # titulos RPG
c = ["guerreiro, ladino, druida"]
classe = input("Digite o nome da classe (Guerreiro, Ladino ou Druida): ").lower().strip()
nivel = int(input("Digite o nivel: "))
item = input("Vc possui algum item especial? (S/N): ").upper().strip()
if classe not in c:
    print("Classe inválida")
elif item == "S":
    if nivel >=30:
        print(f"Você é um {classe} maior")
    else:
        print(f"Você é um {classe} menor")
else:
    print("título: ""sem título""")