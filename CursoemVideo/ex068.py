from random import randint
print('VAMOS JOGAR?????')
cont = 0
while True:
    jog1 = int(input('Digite um valor: '))
    pc = randint(1, 10)
    soma = jog1 + pc
    opc = ' '
    while opc not in 'PI':
        print('PAR / IMPAR')
        opc = str(input('Qual a sua escolha? ')).strip().upper()[0]
    print(f'Você jogou {jog1} e o PC {pc}... Somando {soma}', end='')
    print(' -> DEU PAR' if soma % 2 == 0 else ' -> DEU IMPAR')
    if opc == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU!!!')
            cont += 1
        else:
            print('VOCÊ PERDEU :(')
            break
    if opc == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU!!!')
            cont += 1
        else:
            print('VOCÊ PERDEU :(')
            break
    print('Vamos jogar novamente...')
print('GAME OVER')
print(f'Você conseguiu ganhar {cont} vezes')

