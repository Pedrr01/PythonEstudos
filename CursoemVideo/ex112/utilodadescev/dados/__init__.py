cor = ('\033[0m',  # 0 -Sem Cor
       '\033[31m',  # 1 -Vermelho
       '\033[32m',  # 2-  Verde
       '\033[33m',  # 3 - Amarelo
       '\033[34m',  # 4 - Azul
       '\033[35m',  # 5 - Roxo
       '\033[36m',  # 6 - Branco
       )


def analisador(msg):
    sit = False
    while not sit:
        ent = str(input(msg)).strip().replace('.', ',')
        if ent.isalpha() or ent == '':
            print(f'{cor[1]}ERRO! \'{ent}\' não é um número.\nDigite um valor válido{cor[0]}')
        else:
            sit = True
            return float(ent)
