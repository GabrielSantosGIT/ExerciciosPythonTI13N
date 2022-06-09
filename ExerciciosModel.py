def exercicio01():
    A = 10
    B = 20

    msg = 'Antes da troca: A = {}, B = {}'.format(A, B)
    aux = A
    A = B
    B = aux

    msg = msg + '\n Depois da Troca: A = {}, B = {}'.format(A, B)
    return msg


def exercicio02(num1):
    return num1 - 1

def exercicio03():
    base = int (input ('Informe a base'))
    alt = int (input ('informe a altura'))
    area = base * alt
    return area

def exercicio04():
    ano = int(input ('informe os anos'))
    mes = int(input ('informe os mêses'))
    dia = int(input ('informce os dias'))
    idade: int = ano * 365 + mes * 30 + dia
    return idade
