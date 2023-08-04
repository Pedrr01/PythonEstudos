from math import factorial
print('CALCULO DE FATORIAL')
num = int(input('Digite um valor: '))
c = num
print('O fatorial de {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(factorial(num)), end='')



'''from math import factorial
num = int(input('Digite um valor: '))
print('Claculando o fatorial de {}! ='.format(num), end='')
for c in range(num, 0, -1):
    print(' {}'.format(c), end='')
    print(' x' if c > 1 else ' =', end='')
print(' {}'.format(factorial(num)))'''

