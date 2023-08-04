num1 = float(input('Digite um número:'))
num2 = float(input('Digite um número:'))
num3 = float(input('Digite um número:'))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
print('O menor número é: {}'.format(menor))
# Maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3
print('O maior número é: {}'.format(maior))


