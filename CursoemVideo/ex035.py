a = float(input('Digite o valor da primeira reta:'))
b = float(input('Digite o valor da segunda reta:'))
c = float(input('Digite o valor da terceira reta:'))
print('-=' * 20)
if a < b + c and b < a + c and c < a + b:
    print('Podem Formar Um Triangulo')
else:
    print('Não Podem Formar Um Triangulo')
print('-=' * 20)

