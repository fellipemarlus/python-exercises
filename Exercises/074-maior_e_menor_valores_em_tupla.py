# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

from random import randint

ns = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))


print(f'A tupla aleatória, gerou {ns}')
print(f'O maior número dentro dessa tupla é o {max(ns)}')
print(f'O menor número dentro dessa tupla é o {min(ns)}')
