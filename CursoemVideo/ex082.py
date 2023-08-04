lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opc = ' '
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    while opc not in 'NS':
        opc = str(input('Deseja continuar [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break

print(f'Lista dos números: {lista}')
print(f'Lista dos números pares: {pares}')
print(f'Lista dos números impares: {impares}')
