cor = ('\033[0m',  # 0 -Sem Cor
       '\033[31m',  # 1 -Vermelho
       '\033[32m',  # 2-  Verde
       '\033[33m',  # 3 - Amarelo
       '\033[34m',  # 4 - Azul
       '\033[35m',  # 5 - Roxo
       '\033[36m',  # 6 - Branco
       )


def inteiro(msg):
    sit = False
    while not sit:
        try:
            num = int(input(msg))
        except:
            print(f'{cor[1]}ERRO! Pfv digite um número inteiro válido.{cor[0]}')
        else:
            sit = True
            return num


def alinhamento(msg):
    print(f'{cor[4]}_' * 42)
    print(msg.center(42))
    print(f'_' * 42, cor[0])


def menu(lista):
    alinhamento('MENU DE CADASTRAMENTO')
    for c, o in enumerate(lista):
        print(f'{cor[2]}{c+1} - {o}{cor[0]}')
    print(f'{cor[4]}-' * 42, cor[0])
    resp = inteiro(f'{cor[2]}    --> Sua Opção: {cor[0]}')
    return resp
