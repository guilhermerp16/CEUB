orçamento = float(input("Qual o orçamento? "))
if orçamento >= 100:
  while True:
    n = float(input("Digite o valor do produto: "))
    if n > orçamento:
      print("Produto fora do orçamento")
      break
    else:
      print("Produto dentro do orçamento")
      orçamento -= n
      print(f"Orçamento restante: {orçamento}")
    if orçamento <= 0:
      print("Orçamento esgotado")
      break
else:
  print("orçamento insuficiente")