lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor Adicionado Com Sucesso!!!')
    else:
        print('Valor Duplicado... Irei Descarta!!!')
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja Continuar [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break
lista.sort()
print(f'O valores foram: {lista}')
