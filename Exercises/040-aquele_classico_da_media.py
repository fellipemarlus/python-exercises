# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

import colorama
from colorama import Fore
colorama.init()

print('Programa para calcular a média do seu aluno.')
nome = str(input('Digite o nome do aluno: '))
nt1 = float(input('Digite a nota da primeira prova: '))
nt2 = float(input('Digite a nota da segunda prova: '))
media = (nt1 + nt2) / 2

if media < 5:
    print(f'\nA média do {nome} ficou em {media:.1f}.\n'
          f'{Fore.LIGHTRED_EX}ALUNO REPROVADO{Fore.RESET}')
elif media < 7:
    print(f'\nA média do {nome} ficou em {media:.1f}.\n'
          f'{Fore.LIGHTYELLOW_EX}ALUNO EM RECUPERAÇÃO{Fore.RESET}')
else:
    print(f'\nA média do {nome} ficou em {media:.1f}.\n'
          f'{Fore.LIGHTGREEN_EX}ALUNO APROVADO{Fore.RESET}')
