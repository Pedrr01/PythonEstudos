print('->'* 10,'PROGRAMA 66','<-' * 10)
print('\033[34mCONTAGEM ENCERRA COM 999\033[0m')
cont = soma = 0
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores digitados foi de: {soma}')
