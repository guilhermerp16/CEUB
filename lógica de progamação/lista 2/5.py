nome = input("Digite o nome: ").capitalize()
while len(nome) <= 3:
    nome = input("Nome inválido. Digite novamente: ").capitalize()
idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida. Digite novamente: "))
salario = float(input("Digite o salário: "))
while salario <= 0:
    salario = float(input("Salário inválido. Digite novamente: "))
sexo = input("Digite o sexo (f/m): ").lower()
while sexo != 'f' and sexo != 'm':
    sexo = input("Sexo inválido. Digite novamente (f/m): ").lower()
estado_civil = input("Digite o estado civil (s/c/v/d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Estado civil inválido. Digite novamente (s/c/v/d): ").lower()
print(f"{nome}\n{idade}\n{salario}\n{sexo}\n{estado_civil}")