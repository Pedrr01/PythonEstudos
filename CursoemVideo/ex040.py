nome = str(input('Digite o nome do aluno:')).strip()
nota1 = float(input('Digite a priemira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2

if media >= 6.0:
    print('O aluno {}, foi APROVADO com média: {}'.format(nome, media))
elif media < 6.0 and media >= 5.0:
        print('O aluno {} ficou em RECUPERAÇÂO com média: {}'.format(nome, media))
else:
    print('O aluno {}, foi REPROVADO com média: {}'.format(nome, media))