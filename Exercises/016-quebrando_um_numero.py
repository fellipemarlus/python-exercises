#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num_real = float(input('Digite um número real: '))
conv_int = math.floor(num_real)
print(conv_int)

inteiro = math.trunc(float(input('Digite um número real: ')))
print(f'A parte inteira deste número real é {inteiro}')