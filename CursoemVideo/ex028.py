from time import sleep
import random
valor = int(input('Tente advinhar um número entre 1 e 5:'))
num = random.randint(1,5)
print('PROCESSANDO...')
sleep(3)
print('-='* 20)
if valor == num:
    print('VITORIA, você conseguiu advinhar!')
else:
    print('DERROTA, eu pensei no número {}!'.format(num))
print('-=' * 20)

