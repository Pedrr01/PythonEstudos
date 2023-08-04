pt = int(input('PRIMEIRO TERMO:'))
raz = int(input('RAZÃO:'))
decimo = pt + (10 - 1) * raz
for a in range(pt, decimo + raz, raz):
    print(a, end=' - ')
print('ACABOU!')
