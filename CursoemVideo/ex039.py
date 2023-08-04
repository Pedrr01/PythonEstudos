from datetime import date
nome = str(input('Informe seu nome:')).strip()
nasc = int(input('Qual o ano do seu nascimento?'))
sexo = str(input('Informe o seu sexo: \n [1] Masculino \n [2] Feminino \n Resposta:'))
ano = date.today().year

if (ano - nasc) == 18 and '1' in sexo:
    print('Olá {} você tem 18 anos, esse é o ano do seu alistamento')
elif (ano - nasc) > 18 and '1' in sexo:
    final = (ano - nasc) - 18
    idade = ano - nasc
    print('{} você tem {}, portanto já passou {} anos para seu alistamento'.format(nome, idade, final))
    print('Procure a junta militar mais proxima para regularizar sua documentação')
elif (ano - nasc) < 18 and '1' in sexo:
    final2 = 18 - (ano - nasc)
    idade2 = ano - nasc
    print('{} você tem {}, portanto ainda faltam {} anos para o seu alistamento'.format(nome, idade2, final2))
    print('Fique atento a sua idade, tenha um bom dia!')
else:
    print('Olá {}, mulheres não possuem obrigatoriedade para o alistamento militar'.format(nome))
    print('Tenha um bom dia!')





