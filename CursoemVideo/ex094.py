dic = {}
lista = []
num = []
while True:
    dic.clear()
    dic['nome'] = str(input('Nome: ')).strip()
    dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while dic['sexo'] not in 'MF':
        print('ERRO!!! DIGITE SIM OU NÃO.')
        dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dic['idade'] = int(input('Idade: '))
    num.append(dic['idade'])
    opc = str(input('Deseja continuar [SIM/NÃO]? ')).strip().upper()[0]
    while opc not in 'SN':
        print('ERRO!!! TENTE NOVAMENTE.')
        opc = str(input('Deseja continuar [SIM/NÃO]? ')).strip().upper()[0]
    lista.append(dic.copy())
    if opc == 'N':
        break
print(f'A) Ao todo temos {len(lista)} cadastradas.')
media = sum(num) / len(lista)
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram:')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}')
print('D) As pessoas com idade acima da média foram:')
for b in lista:
    if b['idade'] > media:
        for c, v in b.items():
            print(f'{c} = {v}')





