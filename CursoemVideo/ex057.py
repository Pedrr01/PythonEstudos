nome = str(input('Digite o seu nome: ')).strip()
sexo = str(input('Qual o seu sexo [M/F]: ')).upper()
while sexo not in 'MF':
    print('Sexo invalido...')
    print('Digite uma opção novamente')
    sexo = str(input('Qual o seu sexo [M/F]: ')).upper()
print('DADOS CADASTRADOS COM SUCESSO')