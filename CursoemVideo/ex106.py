from time import sleep
cor = ('\033[0m',  # 0 -Sem Cor
       '\033[0:30:41m',  # 1 -Vermelho
       '\033[0:30:42m',  # 2-  Verde
       '\033[0:30:43m',  # 3 - Amarelo
       '\033[0:30:44m',  # 4 - Azul
       '\033[0:30:45m',  # 5 - Roxo
       '\033[0:30m',  # 6 - Branco
       )


def titulo(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(cor[0], end='')


def manual(com, c=0):
    print(f'Acessando o manual do comando {com}...')
    sleep(2)
    print(cor[c], end='')
    help(com)
    print(cor[0], end='')


# Programa Principal
while True:
    titulo('Interactive Help do Python', 4)
    sleep(1)
    opc = str(input('    -> Função ou Comando: '))
    if opc.upper() == 'FIM':
        break
    else:
        manual(opc, 2)
titulo('VOLTE SEMPRE.', 1)
