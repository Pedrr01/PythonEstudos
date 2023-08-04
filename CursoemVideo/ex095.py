dic = {}
lista = []
time = []
while True:
    dic.clear()
    dic['Nome'] = str(input('Nome: ')).strip()
    part = int(input(f'Quantas partidas o jogador {dic["Nome"]} fez? '))
    lista.clear()
    if part > 0:
        for c in range(1, part+1):
            lista.append(int(input(f'    Quantos gols na {c} partida? ')))
        dic['Gols'] = lista[:]
        dic['Total'] = sum(lista)
        time.append(dic.copy())
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break
print('=' * 30)
print('COD ', end='')
for c in dic.keys():
    print(f'{c:<15}', end='')
print()
print('-' * 30)
for c, v in enumerate(time):
    print(f'{c+1:>3}', end=' ')
    for b in v.values():
        print(f'{str(b):<15}', end='')
    print()
print('=' * 30)
print('DIGITE O COD ou 999 PARA ENCERRAR')
while True:
    busc = int(input('Deseja ver o levantamento de qual jogador? '))
    if busc == 999:
        break
    if busc >= len(time):
        print(f'NÃO FOI ENCONTRADO NENHUM JOGADOR COM O COD {busc}.')
    else:
        print(f'  >>> LEVATAMENTO DO JOGADOR {time[busc]["Nome"]}')
        for c, v in enumerate(time[busc]["Gols"]):
            print(f'  Na {c+1} partida obteve {v} gols.')
print('>>> VOLTE SEMPRE <<<')


