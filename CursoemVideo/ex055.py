maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso é {} e o maior peso é {}'.format(menor, maior))


