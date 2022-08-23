def dobro(valor=0):
    valor *= 2
    return valor


def metade(valor=0):
    valor /= 2
    return valor


def aumento(valor=0, porc=0):
    if porc > 0:
        porc = (valor * porc) / 100
        valor += porc

    return valor


def diminuir(valor=0, porc=0):
    if porc > 0:
        porc = (valor * porc) / 100
        valor -= porc

    return valor


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace(".", ",")

