while True:
    num = int(input('Digite um valor: '))
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    opc = str(input('Deseja Continuar - [SIM/NÃO]? ')).strip().upper()
    if opc in 'NÃO':
        break
print('FIM DO PROGRAMA')
