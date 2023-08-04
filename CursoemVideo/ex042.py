a = float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor:'))
c = float(input('Digite o terceiro valor:'))
print('A soma entre o valores {} {} e {}'.format(a, b, c))

if a < b + c and b < c + a and c < a + b:
    print('PODEM FORMAR UM TRIANGULO')
    if a == b and b == c:
        print('CLASSIFICADO COMO EQUILÁTERO')
    elif a != b != c != a:
        print('CLASSIFICADO COMO ISÓSCELES')
    else:
        print('CLASSIFICADO COMO ESCALENO')
else:
    print('NÂO PODEM FORMAR UM TRIANGULO')


