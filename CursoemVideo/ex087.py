matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mr = []
somap = som3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    mr.append(matriz[l][1])
    print()
print(f'A SOMA DOS PARES RESULTA EM {somap}')
for l in range(0, 3):
    som3 += matriz[l][2]
print(f'A SOMA DA TERCEIRA COLUNA RESULTA EM {som3}')
print(f'O MAIOR NÚMERO DA SEGUNDA COLUNA É {max(mr)} ')




