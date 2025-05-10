# # titulos RPG
classe = input("Digite o nome da classe (Guerreiro, Ladino ou Druida): ").lower().strip()
nivel = int(input("Digite o nivel: "))
item = input("Vc possui algum item especial? (S/N): ").upper().strip()

if classe != "guerreiro" and classe != "ladino" and classe != "druida":
    print("Classe inválida")
elif item == "S":
    if nivel >=30:
        print(f"Você é um {classe} maior")
    else:
        print(f"Você é um {classe} menor")
else:
    print("título: ""sem título""") 
#Me dei a liberdade de adicinar druida ao exercicio, 
#pois o mesmo é minha classe favorita :)