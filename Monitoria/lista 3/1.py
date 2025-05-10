#media de uma lista de números
#função que calcula a média de uma lista de números
def media(lista):
  soma = 0
  for i in lista:
    soma += i
    return  soma / len(lista)
  
lista = []
num = 1

#loop que pede números para o usuário até que ele digite 0
while num != 0:
  num = int(input("digite um número: "))
  lista.append(num)

lista.remove(0)

print(media(lista))