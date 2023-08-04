from random import randint
num = ((randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10), randint(1, 10)))
cont = maior = menor = 0
for c in num:
    print(c, end=' ')
    cont += 1
    if cont == 1:
        maior = menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f'\nO MAIOR NÚMERO FOI {maior}')
print(f'O MENOR NÚMERO FOI {menor}')
# OU FAZER ISSO:
#print(f'\nO MAIOR NÚMERO FOI {max(num)}')
#print(f'O MENOR NÚMERO FOI {min(num)}')

