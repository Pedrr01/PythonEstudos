from ex115.Sistema.interface import *
from time import sleep


def arquiExiste(nome):
    try:
        a = open(nome, 'r')
        a.readable()
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquiCriar(nome):
    try:
        a = open(nome, 'x')
        a.close()
    except:
        print(f'{cor[1]}ERRO AO TENTAR CRIAR O ARQUIVO{cor[0]}')
    else:
        print(f'{cor[3]}ARQUIVO CRIADO COM SUCESSO.{cor[0]}')


def arquiLer(nome):
    try:
        a = open(nome, 'r')
    except:
        print(f'{cor[1]}ERRO AO TENTAR LER O ARQUIVO{cor[0]}')
    else:
        lista = a.readlines()
        for c in lista:
            lista = c.split(';')
            lista[1] = lista[1].replace('\n', '')
            print(f'{lista[0]:<30}{lista[1]:>3} ANOS')
    finally:
        a.close()



def arquiAdc(arq, nome='Desconhecido', idade=0):

    try:
        a = open(arq, 'a')
    except:
        print(f'{cor[1]}ERRO AO TENTAR CRIAR CADASTRO{cor[0]}.')
    else:
        try:
            a.write(f'NOME:{nome}; IDADE:{idade}\n')
            a.close()
        except:
            print(f'{cor[1]}OCORREU UM ERRO NO SISTEMA.{cor[0]}')
        else:
            print(f'{cor[3]}-CADASTRO REALIZADO COM SUCESSO-{cor[0].center(42)}')




