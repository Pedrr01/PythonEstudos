def inteiro(msg):
    sit = False
    while not sit:
        try:
            num = int(input(msg))
        except:
            print('\033[31mERRO!!! Pfv digite um número inteiro válido.\033[0m')
        else:
            sit = True
            print('__' * 30)
            return num


def real(msg):
    sit = False
    while not sit:
        try:
            num2 = float(input(msg))
        except:
            print('\033[31mERRO!!! Pfv digite um número real válido.\033[0m')
        else:
            sit = True
            print('__' * 30)
            return num2
