from random import randint
from time import sleep

itens = ('NADA', 'PAPEL', 'PAPEL', 'TESOURA')
pc = randint(1, 3)
print('Vamos jogar?! \nOpções:')
print('''[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Qual a sua escolha:'))

if jogador > 3:
    print('JOGADA INVALIDA')

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
sleep(1)

print('=-' * 15)
print('PC jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 15)

if pc == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    elif jogador == 3:
        print('PC VENCEU')
elif pc == 2:
    if jogador == 1:
        print('PC VENCEU')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCEU')
elif pc == 3:
    if jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('PC VENCEU')
    elif jogador == 3:
        print('EMPATE')

