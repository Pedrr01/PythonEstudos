dist = float(input('Qual a distancia da viagem:'))
print('Sua vigem de {}Km'.format(dist))
if dist <= 200:
    valor = dist * 0.50
    print('Ficara no valor de R${:.2f}'.format(valor))
else:
    valor1 = dist * 0.45
    print('Ficara no valor de R${:.2f}'.format(valor1))

