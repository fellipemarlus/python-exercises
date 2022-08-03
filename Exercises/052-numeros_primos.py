# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += 1
if total == 2:
    print('O número é primo')
else:
    print('O número não é primo')