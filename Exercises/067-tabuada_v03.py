# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('-----Programa para cálculo de tabuada-----\n')
while True:
    numero = int(input('Digite um número inteiro para ser feito o cálculo: '))
    if numero < 0:
        print('Programa encerrado')
        break
    print('A tabuada de {} é: '.format(numero))
    print('-' * 13)
    for i in range(1, 11):
        tabuada = i * numero
        print(f'{numero} x {i} = {tabuada}')
    print('-' * 13)
    print('Para encerrar o programa, digite um número negativo.\nOu')

