def notas(*n, sit=False):
    """
    -> Funçao para analisar as notas e a situação de varios alunos
    :param n: Resultado obtido por cada aluno
    :param sit:( Opciona ), situação da turma, obtida pela média
    :return: Dicionario com todas as informações
    """
    dic = {}
    dic['Quantidade'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n) / len(n)
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'BOA'
        elif dic['Média'] >= 5:
            dic['Situação'] = 'RAZOAVEL'
        else:
            dic['Situação'] = 'RUIM'
    return dic


# Programa Principal
resp = notas(5.3, 8.5, 9.2, sit=True)
print(resp)
#help(notas)
