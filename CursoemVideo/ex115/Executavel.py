from ex115.Sistema.interface import *
from ex115.Sistema.arquivo import *
from time import sleep

arquivo = 'Sistema CeV.txt'

if not arquiExiste(arquivo):
    arquiCriar(arquivo)


while True:
    dados = menu(['Ver Cadastramentos', 'Realizar Cadastramento', 'Sair do Sistema'])
    if dados == 1:
        print(f'{cor[5]}--> OPÇÃO 1 <--'.center(46), cor[0])
        print('LISTA DE CADASTROS'.center(42))
        print()
        arquiLer(arquivo)
        print()

    elif dados == 2:
        print(f'{cor[4]}--> OPÇÃO 2 <--'.center(44))
        print('---- CADASTRAMENTO ----'.center(46), cor[0])
        print()
        nome = str(input('NOME:')).strip().upper()
        idade = inteiro('IDADE: ')
        arquiAdc(arquivo, nome, idade)


    elif dados == 3:
        print(f'{cor[1]}--> OPÇÃO 3 <--'.center(46))
        print(f'|FINALIZANDO SISTEMA...')
        sleep(1)
        print('|VOLTE SEMPRE')
        sleep(1)
        print('|FIM', cor[0])
        break
    else:
        print(f'{cor[1]}DIGITE UMA OPÇÃO VÁLIDA.{cor[0]}')
        sleep(2)

