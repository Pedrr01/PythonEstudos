from random import randint
print('VAMOS JOGAR?\nVOU PENSAR EM UM NÚMERO ENTRE 0 e 10')
print('TENTE ADVINHAR...')
joga = int(input('Qual o seu número: '))
pc = randint(0, 10)
tent = 0
while joga != pc:
    if joga > pc:
        print('PRA MENOS...\nVOCÊ ERROU, TENTE NOVAMENTE')
        joga = int(input('Qual o seu número: '))
        tent += 1
    elif joga < pc:
        print('PRA MAIS... VOCÊ ERROU, TENTE NOVAMENTE')
        joga = int(input('Qual o seu número: '))
        tent += 1
    elif joga < 10:
        print('OPÇÃO INVALIDA... ESCOLHA UM NÚMERO ENTRE 0 E 10')
        joga = int(input('Qual o seu número: '))
if joga == pc:
    tent += 1
    print('PARABÉNS,VOCÊ GANHOU!!! com {} tentativas'.format(tent))
print('FIM DE JOGO')