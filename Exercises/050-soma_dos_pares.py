# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
print('Vamos somar 6 números inteiros, mas só serão somados, os números que forem pares.')
for i in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if i % 2 == 0:
        soma += n
print(f'Com base nos números que foram digitados, a soma dos pares é {soma}')

