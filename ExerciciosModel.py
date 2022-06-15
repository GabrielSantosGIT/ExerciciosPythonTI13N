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
    base = int(input('Informe a base'))
    alt = int(input('informe a altura'))
    area = base * alt
    return area

def exercicio04():
    ano = int(input('informe os anos'))
    mes = int(input('informe os mêses'))
    dia = int(input('informce os dias'))
    idade: int = ano * 365 + mes * 30 + dia
    return idade

def exercicio05():
    et = int(input('informe o número total de eleitores'))
    vb = int(input('informe o número de votos brancos'))
    vn = int(input('informe o número de votos nulos'))
    vl = int(input('informe o número de votos válidos'))

    pvb = float(vb * 100) / et
    pvn = float(vn * 100) / et
    pvl = float(vl * 100) / et

    result = "A porcentagem de votos brancos é: {}".format(pvb), "A porcentagem de votos nulos é: {}".format(pvn), "A porcentagem de votos válidos é: {}".format(pvl)
    return result

def exercicio06():
    SalarioMensal = float(input('informe o seu salário mensal:'))
    reajuste = float(input('informe o Percentual de reajuste:'))
    newSalario = (SalarioMensal * reajuste / 100) + SalarioMensal
    return newSalario

def exercicio07():
    custoFabrica = float(input('informe o custo de fábrica:'))
    percentualD = custoFabrica * 28 / 100 + custoFabrica
    impostos = custoFabrica * 45 / 100 + custoFabrica
    CustoFinal = "O custo final do seu carro é de: {} R$".format(percentualD + impostos)

    return CustoFinal

def exercicio08():
    nota1 = float(input('informe a 1ª nota do aluno:'))
    nota2 = float(input('informe a 2ª nota do aluno:'))
    nota3 = float(input('informe a 3ª nota do aluno'))
    media = "Sua média Final é: {}".format(nota1 + nota2 + nota3 / 3)

    return media

def exercicio09():
        qntd = (input('informe a quantidade de maçãs'))
        qntd1 = 0
        qntd2 = 0

        if qntd1 < 12:
           qntd1 = 1.30 * qntd
        print("Custo da compra: ", qntd1)

        elif qntd2 >= 12:
             qntd2 = 1.00 * qntd
        print ("Custo da compra: ",qntd2)

