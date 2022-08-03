# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('Vamos calcular e mostrar os 10 primeiros termos de uma Progressão Aritmética')
pt = int(input('Para isso, preciso que você digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * razao

for i in range(pt, decimo + razao, razao):
    print(i, end=' ')
