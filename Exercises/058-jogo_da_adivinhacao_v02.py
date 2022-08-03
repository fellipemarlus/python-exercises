#  Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#  Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

num_comp = randint(1, 10)
numero = int(input('Tente acertar o número que foi escolhido aleatóriamente entre 1 e 10.\n'
                   '\nDigite o seu chute: '))
print('\nAnalisando...'), sleep(2)
tentativas = 1
while numero != num_comp:
    if num_comp == numero:
        tentativas += 1
    else:
        tentativas += 1
        if numero > num_comp:
            print(f'\nVocê errou, tente novamente.')
            print('Chute um número mais baixo ...\n')
            numero = int(input('Tente acertar o número que foi escolhido aleatóriamente entre 1 e 10.\n'
                               'Digite o seu chute: '))
            print('\nAnalisando...'), sleep(2)
        else:
            print(f'\nVocê errou, tente novamente.')
            print('Chute um número mais alto ...\n')
            numero = int(input('Tente acertar o número que foi escolhido aleatóriamente entre 1 e 10.\n'
                               'Digite o seu chute: '))
            print('\nAnalisando...'), sleep(2)



if tentativas == 1:
    print(f'\nParabéns, você acertou o número de PRIMEIRA! O número aleatório é {num_comp}\n'
          f'Você precisou de apenas {tentativas} tentativa.')
else:
    print(f'\nParabéns, você acertou o número! O número aleatório é {num_comp}\n'
              f'Você precisou de {tentativas} tentativas.')