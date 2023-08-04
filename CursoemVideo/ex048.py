soma = 0
cont = 0
for c in range(0, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma entres os {} resulta em: {}'.format(cont, soma))