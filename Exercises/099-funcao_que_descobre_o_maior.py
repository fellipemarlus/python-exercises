# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    cont = maior_n = 0
    print(f'Você digitou os números ', end='')
    for i in num:
        print(f'{i} ', end='')
        if i > maior_n:
            maior_n = i
    print()
    print(f'E o maior valor é o {maior_n}')
    print('~' * 30)


maior(2, 10, 5)
maior(10, 2, 5)
maior(10, 10, 10)
maior(99, 3, 2, 1)
maior(0, 3, 2, 1)