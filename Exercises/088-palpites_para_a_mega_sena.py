# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-' * 52)
print(f'|{"GERADOR DE NÚMEROS PARA A MEGA SENA":^50}|')
print('-' * 52)
qtd = int(input('Digite a quantidade de jogos: '))
jogos = []
temp = []
cont = 0
for n in range(0, qtd):
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            cont = 0
            break
    jogos.append(temp[:])
    temp.clear()
print()
for i, l in enumerate(jogos):
    print(f'O seu {i+1}º jogo: {sorted(l)}')
    sleep(2)
print('\nNúmeros gerados. \n'
      'BOA SORTE !!!')
