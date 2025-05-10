# # Aposentadoria
sexo = input("digite seu sexo M/F: ").upper()
idade = int(input("digite sua idade: "))
contribuiçao = int(input("digite o tempo de contribuicao: "))
if (sexo == "M" and idade >= 66 or contribuiçao >= 36) or (sexo == "F" and idade >= 62 or contribuiçao >= 33):
    print("Aposentadoria aceita")
else:
    print("Aposentadoria negada")