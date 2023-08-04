nome = str(input('Digite o seu nome:')).strip()
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário atual? R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
minimo = sal * 30 / 100
print('Sr.{},a casa no valor de R${:.2f} e com financiamento de {} anos'.format(nome, casa, anos))
print('Séra paga com prestaçõess de R${:.2f} ao mês'.format(prestação))

if minimo >= prestação:
    print('FINANCIAMENTO PODE SER CONCEDIDO')
else:
    print('FINANCIAMENTO NEGADO')