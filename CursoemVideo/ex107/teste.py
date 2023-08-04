import moeda

preço = float(input('Digite o valor: R$ '))
desc = int(input('Desconto: '))

print(f'O produto no valor de {preço} com {desc}% fica por {moeda.aumentar(preço,desc)}')
print(f'O valor {preço} com juros de {desc}% fica por {moeda.diminuir(preço,desc)}')
print(f'O dobro de {preço} é igual a {moeda.dobro(preço)}')
print(f'A metade de {preço} é igual a {moeda.metade(preço)}')