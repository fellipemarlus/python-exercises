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

