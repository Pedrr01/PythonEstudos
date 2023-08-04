from datetime import datetime
dic = {}
dic['NOME'] = str(input('NOME: '))
ano = int(input('ANO DE NASCIMENTO: '))
dic['IDADE'] = datetime.now().year - ano
print('\033[34mDIGITE 0 SE NÃO TIVER CTPS\033[00m')
dic['CTPS'] = int(input('N DA CTPS: '))
if dic['CTPS'] != 0:
    dic['CONTRATAÇÃO'] = int(input('ANO DE CONTRATAÇÃO: '))
    dic['SALÁRIO'] = float(input('SALÁRIO: '))
    dic['APOSENTADORIA'] = dic['IDADE'] + ((dic['CONTRATAÇÃO'] + 35) - datetime.now().year)
for v,c in dic.items():
    print(f'{v} é igual {c}')
