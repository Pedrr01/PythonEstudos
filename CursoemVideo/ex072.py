num = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO',
       'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS',
       'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    opc = int(input('Digite um valor: '))
    if 0 <= opc <= 20:
        print(f'O valor digitado foi \033[31m{num[opc]}\033[00m')
        resp = str(input('DESEJA CONTINUAR [SIM/NÃO]? ')).strip().upper()[0]
        if resp == 'N':
            break
    else:
        print('NÚMERO INVALIDO!!!')
print('FIM DO PROGRAMA')
