pessoas = []
dados = []
num = []
cont = 0
while True:
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    num.append(peso)
    pessoas.append(dados[:])
    cont += 1
    dados.clear()
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja continuar [SIM/NÃO]? ')).strip().upper()[0]
    if opc == 'N':
        break
print(f'Foram Cadastradas {cont} Pessoas.')
maior = max(num)
menor = min(num)
print(f'O maior peso foi de {maior} Kg')
for p in pessoas:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso foi de {menor} Kg')
for p in pessoas:
    if p[1] == menor:
        print(p[0])



