# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from time import sleep
jogador = dict()
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Digite quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = list()
for i in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} marcou na {i+1}ª partida? ')))
jogador['total'] = sum(jogador['gols'])

print('-' * 30)
print(jogador)
print('-' * 30)
sleep(3)
for k, v in jogador.items():
    print(f'O campo {k.upper()} tem o valor {v}')
print('-' * 30)
sleep(3)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'-Na {i+1}ª partida, fez {g} gols')
    sleep(1)
sleep(2)
print(f'Com esses números, {jogador["nome"]} fez um total de {jogador["total"]} gols.')
