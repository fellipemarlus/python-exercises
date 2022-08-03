# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('-' * 30)

saque = int(input('Digite o valor do seu saque: R$'))
cont_50 = cont_20 = cont_10 = cont_1 = 0
while True:
    while saque - 50 >= 0:
        saque -= 50
        cont_50 += 1
    while saque - 20 >= 0:
        saque -= 20
        cont_20 += 1
    while saque - 10 >= 0:
        saque -= 10
        cont_10 += 1
    while saque - 1 >= 0:
        saque -= 1
        cont_1 += 1
    break

if cont_50 != 0:
    print(f'Total de {cont_50} cédulas de R$50.00')
if cont_20 != 0:
    print(f'Total de {cont_20} cédulas de R$20.00')
if cont_10 != 0:
    print(f'Total de {cont_10} cédulas de R$10.00')
if cont_1 != 0:
    print(f'Total de {cont_1} cédulas de R$1.00')
print('-' * 30)
print('Saque realizado com sucesso!')








'''saque = int(input('Digite o valor do saque: '))
while True:
    nota50 = (saque // 50)
    if nota50 % 50 == 0:
        resto50 = 0
        break
    else:
        resto50 = saque - nota50 * 50
    nota20 = (resto50 // 20)
    if nota20 % 20 == 0:
        resto20 = 0
        break
    else:
        resto20 = saque - nota20 * 20


print(f'nota 50 {nota50}')
print(f'nota 20 {nota20}')


#print(nota50)
#print(dif1)
#while True:'''
