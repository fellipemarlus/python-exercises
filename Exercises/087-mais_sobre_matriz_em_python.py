# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma_terc = maior = 0
# alimentando a matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        # somando os pares dentro da matriz
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]

# somando os numeros da terceira coluna
for l in range(0, 3):
    soma_terc += matriz[l][2]
print('-' * 22)

# verificando o maior número da segunda linha
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

# printando na tela a matriz no formato 3x3
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é: {somap}')
print(f'A soma dos valores da terceira coluna é: {soma_terc}')
print(f'O maior número da segunda linha é: {maior}')
