def area(larg, comp):
    tot = larg * comp
    print(f'A aréa de um terreno {larg}x{comp} é de {tot}m²')


print('     CONTROLE DE TERRENO     ')
print('--' * 15)
l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
area(l, c)