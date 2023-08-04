primeiro = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
termo = primeiro
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    c += 1
c2 = int(input('\nQuer mostrar mais quantos termos: '))
c == 11
while c <= c2:
    print('{} ->'.format(termo))
    termo += raz
    c += 1
print('FIM', end='')