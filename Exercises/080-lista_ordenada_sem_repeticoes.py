# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = list()
for i in range(0, 5):
    n = int(input('Digite um número para ser adicionado a lista: '))
    if i == 0:
        numeros.append(n)
    elif n > numeros[-1]:
            numeros.append(n)
    else:
        p = 0
        while p < len(numeros):
            if n <= numeros[p]:
                numeros.insert(p, n)
                break
            p += 1

print(f'\nOs números digitados, foram ordenados: {numeros}')