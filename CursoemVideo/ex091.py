from random import randint
from time import sleep
from operator import itemgetter
jogo = {'JOGADOR 1': randint(1, 6),
        'JOGADOR 2': randint(1, 6),
        'JOGADOR 3': randint(1, 6),
        'JOGADOR 4': randint(1, 6)}
ranking = []
for v, c in jogo.items():
    print(f'O {v} tirou {c}')
    sleep(1)
print('=-=' * 8)
print('>>>>   RANKING   <<<<')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for v, c in enumerate(ranking):
    print(f'{v+1} -> {c[0]} com {c[1]}')
    sleep(1)