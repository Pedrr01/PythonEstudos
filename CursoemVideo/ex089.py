from time import sleep
lista = []
while True:
    nome = str(input('NOME: ')).strip()
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    opc = ' '
    while opc not in 'SN':
        opc = str(input('DESEJA CONTINUAR [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'{"P"}{"NOME":>10}{"MÉDIA":>10}')
for i, c in enumerate(lista):
    print(f'{i}{c[0]:>10}{c[2]:>10}')
print('999 ENCERRA O PROGRAMA')
while True:
    opc = int(input('Digite a posição do aluno que deseja ver: '))
    print(f'O aluno {lista[opc][0]}\nObeteve as notas: {lista[opc][1]}')
    if opc == 999:
        break
print('FINALIZANDO...')
sleep(2)
print('VOLTE SEMPRE!!!')




