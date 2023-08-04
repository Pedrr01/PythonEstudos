from time import sleep

def contador(a, b, c):
    if a < b:
        for c in range(a, b+1, c):
            print(f'{c}', end=' ')
            sleep(1)
        print('-> FIM')
        print()
    else:
        for c in range(a, b+1, c*-1):
            print(f'{c}', end=' ')
            sleep(1)
        print('-> FIM')
        print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(-2, 8, 2)