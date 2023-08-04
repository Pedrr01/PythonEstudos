dic = {'NOME': str(input('NOME: ')),
       'MÉDIA': float(input('MÉDIA: ')),
       'SITUAÇÃO': ' '}
print('=-=' * 5)
if dic['MÉDIA'] >= 7:
    dic['SITUAÇÃO'] = 'APROVADO'
elif 7 > dic['MÉDIA'] >= 5:
    dic['SITUAÇÃO'] = 'RECUPERAÇÃO'
else:
    dic['SITUAÇÃO'] = 'REPROVADO'
print(f'O ALUNO(A) {dic["NOME"]} está {dic["SITUAÇÃO"]} ')



