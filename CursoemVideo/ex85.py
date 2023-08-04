lista = [[], []]
print('DIGITE 999 PARA PARAR O PROGRAMA')
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
    if num == 999:
        break
n = sorted(lista[0])
p = sorted(lista[1])
print(f'PARES: {n}\nIMPARES: {p}')
