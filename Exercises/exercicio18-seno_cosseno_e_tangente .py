# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno do angulo é: {seno:.2f}\nO cosseno do angulo é: {cosseno:.2f}\nA tangente do angulo '
      f'é: {tangente:.2f}')