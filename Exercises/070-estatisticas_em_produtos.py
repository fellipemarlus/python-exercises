# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('Registrador de Produtos\n')

total = cont_mil = cont = menor = 0
prod_barato = ''
while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()
    preco = float(input('Digite o preço do produto: R$'))
    total += preco
    cont += 1

    if preco > 1000:
        cont_mil += 1

    if cont == 1 or preco < menor:
        menor = preco
        prod_barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer registrar mais produtos? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-' * 15)
print('Com esses produtos registrados, temos as seguintes informações: ')
print(f'O total gasto nessa compra, é de R${total:.2f}')
print(f'Registramos {cont_mil} produtos com valor acima de R$1000.00')
print(f'Registramos o produto com o nome de {prod_barato}, como o de menor valor')
