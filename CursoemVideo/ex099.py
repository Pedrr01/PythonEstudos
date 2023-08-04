from time import sleep

def contador(*num):
    print('Analisando os valores...')
    sleep(2)
    cont = 0
    for c in num:
        print(f'{c}', end=' ')
        cont += 1
        sleep(1)
    print(f'Foram informados {cont} ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('-=' * 20)


contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)