dic = {}
lista = []
dic['nome'] = str(input('Nome: ')).strip()
part = int(input(f'Quantas partidar o jogador {dic["nome"]} fez? '))
if part > 0:
    for c in range(1 , part + 1):
        gols = int(input(f'    Quantos gols na {c} partida? '))
        lista.append(gols)
else:
    print(f'O jogador {dic["nome"]} não realizou nenhum jogo!!!')
dic['gols'] = lista[:]
dic['total'] = sum(lista)
print('=-=' * 10)
for c, v in dic.items():
    print(f'O campo {c} tem o valor igual {v}')
print('=-=' * 10)
print(f'O {dic["nome"]} jogou {part} partidas.')
for c, v in enumerate(lista):
    print(f'    -> Na {c+1} partida ele fez {v} gols.')