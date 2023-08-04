def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 15:
        return 'VOTO NEGADO'
    elif 18 <= idade < 70:
        return 'VOTO OBRIGATORIO'
    else:
        return 'VOTO OPICIONAL'


nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))



