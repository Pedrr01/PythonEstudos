from math import pow, sqrt
op = float(input('Digite o valor do cateto oposto:'))
ad = float(input('Digite o valor do cateto adjacente:'))
soma1 = (pow(op, 2) + (pow(ad, 2)))
print('O valor da hipotenusa é de:{:.2f}'.format(sqrt(soma1)))
