sal = float(input('Digite o seu salário:R$'))
if sal >= 1250.00:
    valor = 10/100 * sal
    print('O seu salário atual com aumento de 10%')
    print('É de: R${:.2f}'.format(valor + sal))
else:
    valor1 = 15 / 100 * sal
    print('O seu salário atual com aumento de 15%')
    print('É de: R${:.2f}'.format(valor1 + sal))
