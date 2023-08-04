def ficha(nome = '<desconhecido>', gol = 0):
    return f'O joagdor {nome}, marcou um total de {gol} gol(s).'


jogador = str(input('Nome: '))
gols = str(input('Gols: '))

if jogador.strip() == '':
    jogador = '<desconhecido>'
if gols.isnumeric():
    gols = gols
else:
    gols = 0
print(ficha(jogador, gols))
