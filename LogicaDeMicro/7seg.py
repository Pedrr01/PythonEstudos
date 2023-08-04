from time import sleep
from cores import cor
print(cor[3], '=-=' * 10)
print(f'{"DISPLAY 7SEG".center(30)}')
print('-=-' * 10, cor[0])
print('--> ADC (+)\n--> DIM (-)\n-> SAIR (f)')
seg7 = [
    [0],  # 0
    [1],  # 1
    [2],  # 2
    [3],  # 3
    [4],  # 4
    [5],  # 5
    [6],  # 6
    [7],  # 7
    [8],  # 8
    [9]  # 9
]
cont = 0
while True:
    try:
        bot = str(input('QUAL SUA OPÇÃO? '))
    except:
        print(cor[1],'HOUVE UM ERRO TENTE NOVAMENTE...', cor[0])
    else:
        print(cor[3],'-' * 30, cor[0])
        if cont == 0 and bot == '-' or cont == 9 and bot == '+':
            print(end='')
        elif bot == '+':
            cont += 1
        elif bot == '-':
            cont -= 1
        elif bot.lower() == 'f':
            print('FINALIZANDO...')
            sleep(3)
            print('FIM.')
            break
        print(cor[2], seg7[cont], cor[0])


