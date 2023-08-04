nome = str(input('Digite o seu nome:'))
peso = float(input('Qual o seu peso:'))
alt = float(input('Qual a sua altura:'))
imc = peso / alt ** 2

if imc < 18.5:
    print('Olá {}, você se encontra abaixo do peso com o IMC = {:.2f}'.format(nome, imc))
elif imc >= 18.5 and imc < 25:
    print('Olá {}, você se enconta no peso ideal com o IMC = {:.2f}'.format(nome, imc))
elif imc >= 25 and imc < 30:
    print('Olá {}, você se encontra em sobrepeso com o IMC = {:.2f}'.format(nome, imc))
elif imc >= 30 and imc < 40:
    print('Olá {}, você se encontra em estado de obesidade com o IMC = {:.2f}'.format(nome, imc))
else:
    print('Olá {}, você se encontra em estado de Obesidade Mórbida com o IMC = {:.2f}'.format(nome, imc))