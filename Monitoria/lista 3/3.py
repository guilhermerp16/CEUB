alunos = {}
turma = 0

#solicitando o número de alunos
while True:
    try:
        turma = int(input("Digite o número de alunos: "))
        if turma <= 0:
            print("O número de alunos deve ser maior que zero.")
            continue
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Adicionando alunos e notas ao dicionário
for i in range(turma):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

# Exibindo os alunos com nota maior ou igual a 8
for aluno, nota in alunos.items():
    if nota >= 8:
        print(f"{aluno}: {nota}")

#média da turma
media = sum(alunos.values()) / len(alunos)
print(f"A média da turma é: {media:.2f}")