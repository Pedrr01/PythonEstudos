from time import sleep
print('<>' * 10, 'CASDASTRO', '<>' * 10)
tot18 = toth = totf20 = 0
while True:
    print('=-=' * 10)
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = ' '
    if idade >= 18:
        tot18 += 1
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    print('=-=' * 10)
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade <= 20:
        totf20 += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('DESEJA CONTINUAR - [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break
print('ANALISANDO DADOS...')
sleep(3)
print(f'Foram cadastrados {tot18} pessoas de maior')
print(f'Foram cadastrados {toth} homens')
print(f'Foram cadastras {totf20} mulheres com menos de 20 anos')
