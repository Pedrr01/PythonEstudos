soma = 0
media = 0
hvelho = 0
nomevelho = ''
m20 = 0
for p in range(1, 5):
    print('---- {} PESSOA ----'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    soma += idade
    if idade == 1 and sexo in 'M':
        hdvelho = idade
        nomevelho = nome
    if idade > hvelho:
        hvelho = idade
        nomevelho = nome
    if idade < 20 and sexo in 'F':
        m20 += 1
media = soma / 4
print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho é {} com {} anos'.format(nomevelho, hvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(m20))

