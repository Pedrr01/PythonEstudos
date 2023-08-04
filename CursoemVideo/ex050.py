cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Os {} números PARES somados resultam em: {}'.format(cont, soma))

















