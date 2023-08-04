print('-'*10, ' LOJAS AMERICANAS ', '-'*10)
soma = cont = cont2 = menor = 0
barato = ''
while True:
    print('=-=' * 15)
    nome = str(input('NOME DO PRODUTO: '))
    preço = float(input('PREÇO: R$ '))
    soma += preço
    cont2 += 1
    if cont2 == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    if preço > 1000:
        cont += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('DESEJA CONTINUAR [SIM/NÃO]? ')).strip().upper()[0]
    print('=-=' * 15)
    if opc == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da sua compra foi de R${soma}')
print(f'Temos {cont} custando mais que R$1000')
print(f'O menor preço foi do {barato} custando {menor}')
