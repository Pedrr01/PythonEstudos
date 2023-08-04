lista = ('BRAHMA', 2.99,
         'HEINEKEN', 5.79,
         'BUDWEISER', 3.99,
         'STELLA', 4.19,
         'SKOL', 2.99,
         'CORONA', 5.99,
         'ITAIPAVA', 2.99)
print('-'*37)
print(f'{"PREÇO DAS BEBIDAS":^37}')
print('-'*37)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f' R${lista[c]:.2f}')
print('-'*37)


