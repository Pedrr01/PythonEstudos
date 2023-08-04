def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('\033[31mERRO!!! Digite um valor valido.\033[0m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'O valor digitado foi {n}.')
