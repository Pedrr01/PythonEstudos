cont = soma = 0
num = int(input('Digite um valor: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor: '))
print('A soma dos {} valores, resultam em: {}'.format(cont, soma))