num = (int(input('Digite o 1 número: ')),
       int(input('Digite o 2 número: ')),
       int(input('Digite o 3 número: ')),
       int(input('Digite o 4 número: ')))
print(f'Os números digitados froam {num}')
print(f'O número NOVE aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número TRÉS aparece na {num.index(3)+1} posição')
else:
    print('O NÚMERO 3 NÃO FOI DIGITADO')
print(f'Os números PARES digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
print(f'\nOs números IMPARES digitados foram: ', end='')
for b in num:
    if b % 2 == 1:
        print(b, end=' ')



