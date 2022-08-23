# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

precos = ('Televisão', 5350,
          'Monitor Gamer', 2100,
          'Pc Gamer', 4599,
          'Mouse', 150.99,
          'Teclado', 215.80,
          'Cadeira', 699.99,
          'Mesa', 1050.49)
print(f'\n{"Lista de Produtos":^40}\n')
for i in range(0, len(precos)):
    if i % 2 == 0:
        print(f'{precos[i]:.<30}', end='')
    else:
        print(f'R${precos[i]:.2f}')