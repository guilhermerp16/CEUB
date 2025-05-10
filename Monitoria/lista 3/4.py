#objetos do programa:
digitados = []
sorteados = []
acertos = 0
import random

#Solicita ao usuário 5 números entre 1 e 50
for i in range(5):
    num = int(input("Digite um número de 1 a 50: "))
    while num < 1 or num > 50 or num in digitados:
        print("Número inválido ou já digitado. Tente novamente.")
        num = int(input("Digite um número de 1 a 50: "))
    digitados.append(num)

#Sorteia 5 números entre 1 e 50    
for i in range(5):
    num = random.randint(1, 50)
    while num in sorteados:
        num = random.randint(1, 50)
    sorteados.append(num)

#conta quantos números o usuário acertou
for i in digitados:
    if i in sorteados:
        acertos += 1

#Exibe os resultados        
print("Você acertou", acertos, "números.")
print("Seus números foram:", digitados)
print("Números sorteados foram:", sorteados)
print("Os números que você acertou foram:", end=" ")
for i in digitados:
    if i in sorteados:
        print(i, end=" ")