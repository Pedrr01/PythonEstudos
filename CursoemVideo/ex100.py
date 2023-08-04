from time import sleep
from random import randint

def sorteia(num):
    print('SORTEANDO 5 VALORES...')
    sleep(1)
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    for v in lista:
        print(f'{v}', end=' ')
        sleep(1)
def somapar(num):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores PARES foi de {soma}')


lista = []
sorteia(lista)
somapar(lista)
