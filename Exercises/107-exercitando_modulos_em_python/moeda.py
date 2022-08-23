def dobro(valor):
    valor *= 2
    return f"{valor:.2f}"


def metade(valor):
    valor /= 2
    return f"{valor:.2f}"


def aumento(valor, porc=0):
    if porc > 0:
        porc = (valor * porc) / 100
        valor += porc

    return f"{valor:.2f}"


def diminuir(valor, porc=0):
    if porc > 0:
        porc = (valor * porc) / 100
        valor -= porc

    return f"{valor:.2f}"


