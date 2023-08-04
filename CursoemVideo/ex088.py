from random import randint
print('<>' * 15)
print(f'{"MEGA SENA":^30}')
print('<>' * 15)
lista1 = []
listap = []
cont2 = 1
opc = int(input('Quantos jogos você deseja? '))
while cont2 <= opc:
    cont1 = 0
    while True:
        num = randint(1, 60)
        if num not in lista1:
            lista1.append(num)
            cont1 += 1
        if cont1 >= 6:
            break
    lista1.sort()
    listap.append(lista1[:])
    lista1.clear()
    cont2 += 1
for i, c in enumerate(listap):
    print(f'{i + 1} {c}')







