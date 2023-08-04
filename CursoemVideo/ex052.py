num = int(input('Digite um valor:'))
cont = 0
soma = 0
for c in range(1, num):
    if num % c == 0:
        print('\033[31m', end='')
        cont += 1
        soma += c
    else:
        print('\033[32m', end='')
    print('{}'.format(c), end='')
if cont == 2:
    print('\033[34m\nO {} é divisvel por {} números por isso ele é um NÚMERO É PRIMO'.format(num, cont))
else:
    print('\033[34m\nO {} é divisivel por {} números por isso ele NÃO É PRIMO'.format(num, cont))


