print('<>' * 20)
print('{:^45}'.format('\033[34mBANCO PVS\033[0m'))
print('<>' * 20)
valor = int(input('INFORME O VALOR DO SAQUE: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'TOTAL DE {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=-=' * 13)
print('VOLTE SEMPRE AO BANCO PVS!')

