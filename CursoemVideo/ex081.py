lista = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    cont += 1
    lista.append(num)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break

print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado!!!')
else:
    print('O valor 5 não foi encontrado!!!')
