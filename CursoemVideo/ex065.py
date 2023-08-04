opc = 1
cont = soma = maior = menor = 0
while opc == 1:
    num = int(input('Digite um valor: '))
    print('Quer continuar?\n[1]SIM\n[2]NÂO')
    opc = int(input('Qual a sua escolha? '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('A soma entre os {} valores informados é de: {}'.format(cont, soma))
print('Com uma media de {}'.format(media))
print('O MAIOR número informado foi: {}\nO MENOR número informado foi: {}'.format(maior, menor))


