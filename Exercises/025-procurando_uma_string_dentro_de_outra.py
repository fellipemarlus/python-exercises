# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

print('Vamos analisar você tem o nome SILVA no seu nome!')
nome = input('Digite seu nome completo:').strip().upper()

if nome.__contains__('SILVA'):
    print('Seu nome possui Silva')
else:
    print('Seu nome não possui Silva')


'''print('Vamos analisar você tem o nome SILVA no seu nome!')
nome = input('Digite seu nome completo:').strip().upper()

print(f'Seu nome possui Silva ? {"SILVA" in nome}')'''
