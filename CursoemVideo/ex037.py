num = int(input('Digite um valor inteiro:'))
print('Escolha a base de conversão:')
base = str(input(' [1] para binário \n [2] para octal \n [3] para hexadecimal \n Resposta:'))

if '1' in base:
    valor = bin(num)
    print('O número {} em Binário fica: {}'.format(num , valor[2:]))
elif '2' in base:
    valor1 = oct(num)
    print('O número {} em Octal fica: {}'.format(num, valor1[2:]))
elif '3' in base:
    valor2 = hex(num)
    print('O número {} em Hexadecimal fica: {}'.format(num, valor2[2:]))
else:
    print('Base Não Informada!')



