print(('40=^'.format('LOJAS AMERICANAS')))
valor = float(input('Digite o valor do produto:'))
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')
pag = str(input('Escolha o metodo de pagamento:'))

if '1' in pag:
    total = (valor * 10) / 100
    print('O produto que custa {} ficara por {} se for comprado á vista no dinheiro/cheque'.format(valor, valor - total))
elif '2' in pag:
    total1 = (valor * 5) / 100
    print('O produto que custa {} ficara por {} se for comprado á vista no cartão'.format(valor, valor - total1))
elif '3' in pag:
    total2 = valor / 2
    print('O produto que custa {} ficara em 2x de {} no cartão'.format(valor, total2))
elif '4' in pag:
    pag2 = int(input('Em quantas vezes deseja dividir:'))
    total3 = (((valor * 20) / 100) + valor) / pag2
    print('O produto que custa {} ficara em {}x de {} no cartão'.format(valor, pag2, total3))
else:
    print('OPÇÃO NÃO INFORMADA')