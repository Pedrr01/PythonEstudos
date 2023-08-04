def fac(num, show):
    """
    :param num: Valor a ser calculado
    :param show: OPCIONAL (Mostra a resolução ou não)
    :return: O valor
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f' {c} =', end='')
            else:
                print(f' {c} x', end='')
    return f


print(fac(5, True))