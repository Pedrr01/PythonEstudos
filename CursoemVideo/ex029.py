vel = float(input('Qual a velocidade do carro?'))
multa = (vel - 80) * 7
if vel > 80:
    print('Seu carro foi multado!')
    print('O valor a pagar é de: {:.2f}'.format(multa))
else:
    print('Seu carro está no limite permitido!')
    print('Tenha uma otima viagem!')
