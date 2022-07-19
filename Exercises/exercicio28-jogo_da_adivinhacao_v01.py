# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num_comp = randint(0, 5)
numero = int(input('Tente acertar o número que foi escolhido aleatóriamente entre 0 e 5.\n'
                   'Digite o seu chute: '))

print('Analisando...'), sleep(2)

if num_comp == numero:
    print(f'Parabéns, você acertou o número! O número aleatório é {num_comp}')
else:
    print(f'Você errou, o número escolhido aleatóriamente foi {num_comp}, tente novamente.')
