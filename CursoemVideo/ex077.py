palavras = ('Pedro', 'Programador', 'Intenet', 'Dinheiro', 'Sucesso', 'Sonho')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for b in c:
        if b.lower() in 'aeiou':
            print(b, end=' ')