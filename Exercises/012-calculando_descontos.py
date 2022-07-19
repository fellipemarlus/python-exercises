# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Vamos calcular um desconto de 5% no valor de um produto.')

produto = float(input('Digite o valor do produto: '))
desc = produto - (produto * 5 / 100)
print(f'O valor inicial do produto é de R${produto:.2f}, com o desconto de 5%, o valor cai para R${desc:.2f}')