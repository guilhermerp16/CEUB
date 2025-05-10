classes = ['druida', 'mago', 'guerreiro', 'ladino']
def dia():
    for i in range(4):
        print(f'{i+1} - {classes[i]}')
    escolha = int(input('Escolha sua classe: '))
    if escolha > 4:
        print('Classe inválida')
    elif escolha < 1:
        print('Classe inválida')
    elif escolha == 1:
        print('Você escolheu druida')
    elif escolha == 2:
        print('Você escolheu mago')
    elif escolha == 3:
        print('Você escolheu guerreiro')
    elif escolha == 4:
        print('Você escolheu ladino')
    else:
        print('Classe inválida')
escolha = 0
dia()