dias = int(input('Qual a quantidade de dias?'))
km = float(input('Qual a quantidade de Km rodados?'))
s1 = dias * 60
s2 = km * 0.15
print('O preço a se pagar é de R${:.2f}'.format(s1+s2))