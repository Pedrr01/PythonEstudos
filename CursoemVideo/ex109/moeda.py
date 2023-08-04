cor = ('\033[0m',  # 0 -Sem Cor
       '\033[31m',  # 1 -Vermelho
       '\033[32m',  # 2-  Verde
       '\033[33m',  # 3 - Amarelo
       '\033[34m',  # 4 - Azul
       '\033[35m',  # 5 - Roxo
       '\033[36m',  # 6 - Branco
       )


def aumentar(num=0, taxa=0, formato=False):
    rest = num + (num * taxa / 100)
    return rest if formato is False else form(rest)


def diminuir(num=0, taxa=0, formato=False):
    rest = num - (num * taxa / 100)
    return rest if formato is False else form(rest)


def dobro(num=0, formato=False):
    rest = num * 2
    return rest if formato is False else form(rest)


def metade(num=0, formato=False):
    rest = num / 2
    return rest if formato is False else form(rest)


def form(num, moeda='R$'):
    return f'{cor[2]}{moeda}{num:.2f}{cor[0]}'.replace('.', ',')
