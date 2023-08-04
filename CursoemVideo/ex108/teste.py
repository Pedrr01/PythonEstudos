import moeda

p = float(input('Digite o valor: '))
d = int(input('Desconto: '))

print(f'O dobro de {moeda.form(p)} é {moeda.form(moeda.dobro(p))}')
print(f'A metade de {moeda.form(p)} é {moeda.form(moeda.metade(p))}')
print(f'Aumentando {d}%, ficamos com {moeda.form(moeda.aumentar(p,d))}')
print(f'Diminuindo {d}%, ficamos com {moeda.form(moeda.diminuir(p,d))}')