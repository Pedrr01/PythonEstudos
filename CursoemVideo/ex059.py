from time import sleep
num1 = float(input('Digite o primerio valor: '))
num2 = float(input('Digite o segundo valor: '))
opc = 0
while opc != 5:
    opc = int(input('''
    [1] SOMA
    [2] MULTIPLICAÇÂO
    [3} QUAL O MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
->->->-> Escolha uma opção: '''))
    if opc == 1:
        print('A SOMA entre {} + {} = {}'.format(num1, num2, num1 + num2))
    elif opc == 2:
        print('O MUTIPLICAÇÃO ente {} x {} = {}'.format(num1, num2, num1 * num2))
    elif opc == 3:
        num1 > num2
        maior = num1
        if num1 < num2:
            maior = num2
        print('O maior número entre {} e {} é: {}'.format(num1, num2, maior))
    elif opc == 4:
        print('Digite os novos valores...')
        num1 = float(input('Digite o primerio valor: '))
        num2 = float(input('Digite o segundo valor: '))
    elif opc == 5:
        print('FINALIZANDO...')
        sleep(2)
        print('FIM DO PROGRAMA!')
    else:
        print('\033[34mOPÇÂO INVALIDA, faça uma nova escolha...\033[0m')





