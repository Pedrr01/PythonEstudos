from datetime import date
nome = str(input('Digite o nome do atleta:'))
data = int(input('Digite o ano de nascimento do atleta:'))
ano = date.today().year - data
if ano <= 9:
    print('O atleta {} tem {} anos e está na categoria MIRIM'.format(nome, ano))
elif ano <= 14 and ano > 9:
    print('O atleta {} tem {} anos e está na categoria INFANTIL'.format(nome, ano))
elif ano <= 19 and ano > 14:
    print('O atleta {} tem {} anos e está na categoria JÚNIOR'.format(nome, ano))
elif ano <= 25 and ano > 19:
    print('O atleta {} tem {} anos e está na categoria SÊNIOR'.format(nome, ano))
else:
    print('O atleta {} tem {} anos e está na categoria MASTER'.format(nome, ano))
