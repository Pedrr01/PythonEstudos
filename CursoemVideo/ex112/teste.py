from ex112.utilodadescev import moeda
from ex112.utilodadescev import dados

p = dados.analisador('Digite o preço: R$')
aum = int(input('Informe a taxa de aumento: '))
red = int(input('Informe a taxa de redução: '))
moeda.resumo(p, aum, red)