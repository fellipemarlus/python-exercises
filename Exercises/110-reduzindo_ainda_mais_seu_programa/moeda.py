def dobro(valor=0, format=False):
    valor *= 2
    return valor if format is False else moeda(valor)


def metade(valor=0, format=False):
    valor /= 2
    return valor if format is False else moeda(valor)


def aumento(valor=0, porc=0, format=False):
    if porc > 0:
        porc = (valor * porc) / 100
        valor += porc
    return valor if format is False else moeda(valor)


def diminuir(valor=0, porc=0, format=False):
    if porc > 0:
        porc = (valor * porc) / 100
        valor -= porc
    return valor if format is False else moeda(valor)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace(".", ",")


def resumo(valor=0, aum=10, dim=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{moeda(valor)}')
    print(f'Dobro do valor: \t{dobro(valor, True)}')
    print(f'Metado do valor: \t{metade(valor, True)}')
    print(f'Aumento de {aum}%: \t{aumento(valor, aum, True)}')
    print(f'Redução de {dim}%: \t{diminuir(valor, dim, True)}')

