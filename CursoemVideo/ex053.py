pal = str(input('Digite algo:')).strip().upper()
separa = pal.split()
junto = ''.join(separa)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('A FRASE É UM PALÍNDROMO!')
else:
    print('A FRASE NÃO É UM PALÍNDROMO')

