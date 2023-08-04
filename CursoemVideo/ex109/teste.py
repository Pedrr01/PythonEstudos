from ex109 import moeda

p = float(input('Digite o valor: '))
d = int(input('Desconto: '))

print(f'O dobro de {moeda.form(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.form(p)} é {moeda.metade(p, True)}')
print(f'Aumentando {d}%, ficamos com {moeda.aumentar(p,d, True)}')
print(f'Diminuindo {d}%, ficamos com {moeda.diminuir(p,d, True)}')