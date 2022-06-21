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
    if base <= 0:
        return 'por favor, digite um valor positivo!'
    elif  alt <= 0:
        return 'por favor, digite um valor positivo!'
    else:
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
    maca = int(input('informe a quantidade de maçãs'))
    if maca >= 12:
       total = maca
       msg = '\n custo total da compra: {}'.format(total)
       return msg

    else:
       maca <= 12
       total2 = maca * 1.30
       msg1 = '\n custo total da compra: {}'.format(total2)
       return msg1

def exercicio10():
    vet = []
    for i in range(10):
        valor = int(input('informe o {}º valor: '.format(i+1)))
        vet.append(valor)

    vet.sort()
    print('Os números em Ordem são: {}'.format(vet))

def exercicio11():
    sFixo = float(input('informe o Salário Fixo'))
    vVendas =  float(input('informe o valor de Vendas'))

    if vVendas <= 1500:
        Stotal1 =  vVendas * 3 /100 + vVendas + sFixo
        msg =  '\n Salário total: {}'.format(Stotal1)
        return msg

    elif vVendas > 1500:
        Stotal2 = vVendas * 5 /100 + vVendas + sFixo
        msg1 ='\n Salário total: {}'.format(Stotal2)
        return msg1

def exercicio12():
    NumConta = float(input('informe o número da conta:'))
    Saldo =  float(input('informe o saldo da conta: '))
    debito = float(input ('informe o debito da conta: '))
    credito = float(input ('informe o credito da conta:'))


