lista = []
cont = menor = maior = 0
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c} valor: ')))
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor foi {max(lista)} na posição {lista.index(max(lista))+1}')
print(f'O menor valor foi {min(lista)} na posição {lista.index(min(lista))+1}')




