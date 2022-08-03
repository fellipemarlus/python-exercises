# Crie um programa que faça o computador jogar Jokenpô com você.

import random
print('GAME PEDRA PAPEL E TESOURA')
print('Suas opções para jogar\n'
      '(0) PEDRA\n'
      '(1) PAPEL\n'
      '(2) TESOURA\n')

opcoes = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
jogador = int(input('Digite a sua opção de jogada: '))
print(f'Você jogou {opcoes[jogador]}')
print(f'O computador jogou {opcoes[pc]}')

if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU')
    else:
        print('Jogada inválida')
elif pc == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('Jogada inválida')
elif pc == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')