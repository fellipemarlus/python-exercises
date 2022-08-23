# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dados = []
pessoas = []
p_leves = []
p_pesadas = []
qt_pessoas = 0

while True:
    nome = str(input('Digite o nome da pessoa: '))
    peso = float(input('Digite o peso da pessoa: '))
    dados.append(nome)
    dados.append(peso)
    if peso < 70:
        p_leves.append(dados[:])
    elif peso > 100:
        p_pesadas.append(dados[:])
    pessoas.append(dados[:])
    qt_pessoas += 1
    dados.clear()
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja adicionar mais dados ? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        break

print(f'\nForam cadastradas {qt_pessoas} pessoas.')
print(f'\nO nome das pessoas mais leves: ', end='')
for p in p_leves:
    print(f'[{p[0]}]', end=' ')
print(f'\nPesando respectivamente: ', end='')
for p in p_leves:
    print(f'{p[1]}Kg', end=' ')

print(f'\nO nome das pessoas mais pesadas: ', end='')
for p in p_pesadas:
    print(p[0], end=' ')
print()
print(f'\nPesando respectivamente: ', end='')
for p in p_pesadas:
    print(f'{p[1]}Kg', end=' ')
