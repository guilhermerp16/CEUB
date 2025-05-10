primeiro = int(input("Digite um número: "))
segundo = int(input("Digite outro número: "))
while primeiro > segundo:
    print("O primeiro número é maior que o segundo, digite novamente: ")
    primeiro = int(input("Digite um número: "))
    segundo = int(input("Digite outro número: "))
#caso queira pedir somente o primeiro número novamente:
#while primeiro > segundo:
#   primeiro = int(input("O primeiro número é maior que o segundo, digite novamente: "))