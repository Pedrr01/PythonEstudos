exp = str(input('Digite uma expressão: '))
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha == 0:
    print('Expressão Valida!!!')
else:
    print('Expressão Invalida!!!')