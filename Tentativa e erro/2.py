primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
comparacao = input("Digite o tipo de comparação: (==, !=, >, <, >=, <=): ")
if comparacao == "==":
    resultado = primeiro == segundo 
elif comparacao == "!=":
    resultado = primeiro != segundo
elif comparacao == ">":
    resultado = primeiro > segundo
elif comparacao == "<":
    resultado = primeiro < segundo
elif comparacao == ">=":
    resultado = primeiro >= segundo
elif comparacao == "<=":
    resultado = primeiro <= segundo
else:
    resultado = "Operador inválido"
print(f"Resultado: {resultado}")
# Comparação de números