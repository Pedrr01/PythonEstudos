num1 = float(input('Digite o primeiro valor:'))
num2 = float(input('Digite o segundo valor:'))

if num1 > num2:
    print('O número {} é maior que o numero {}!'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior do que o número {}!'.format(num2, num1))
else:
    print(' Os numeros {} e {} \n Possuem o mesmo valor!'.format(num1, num2))
