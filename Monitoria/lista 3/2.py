palavra = input("Digite uma palavra: ").lower()
vogais = "aeiouáéíóúãõâêîôûãõêô"
consoantes = "bcdfghjklmnpqrstvwxyz"
contagem_vogais = 0
contagem_consoantes = 0
for letra in palavra:
    if letra in vogais:
        contagem_vogais += 1
    elif letra in consoantes:
        contagem_consoantes += 1
print("A palavra tem", contagem_vogais, "vogais e", contagem_consoantes, "consoantes.")