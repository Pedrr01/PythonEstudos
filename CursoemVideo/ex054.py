from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Qual o ano de nasciemnto da {} pessoa:'.format(c)))
    anos = atual - nasc
    if anos >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Das 7 pessoas {} são de MAIOR'.format(totmaior))
print('Das 7 pesssoas {} são de MENOR'.format(totmenor))


