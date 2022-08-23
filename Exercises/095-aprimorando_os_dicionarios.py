# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep
lista_jogadores = []
while True:
    jogador = dict()
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Digite quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    for i in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} marcou na {i+1}ª partida? ')))
    jogador['total'] = sum(jogador['gols'])
    lista_jogadores.append(jogador.copy())
    while True:
        continuar = str(input('Você quer adicionar informações de outro jogador ? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('OPÇÃO INVALIDA! Digite apenas S (Sim) ou N (Não).')
    if continuar == 'N':
        break
print(f'\nInformações adicionadas.'
      f'\nGerando tabela... '), sleep(2)

print(lista_jogadores)
print('-' * 40)
#print(f'{"Nº":<4} {"NOME":<15} {"GOLS":<15} {"TOTAL":<15}')
print('COD ', end='')
for i in jogador.keys():
    print(f'{i.upper():<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(lista_jogadores):
    print(f'{k:<4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    cod = int(input('Conforme os códigos da tabela gerada, você quer ver os dados de algum jogador?\n'
                    'Digite o código do jogador ou [999] para terminar o programa: '))
    if cod == 999:
        break
    if cod >= len(lista_jogadores):
        print(f'ERRO, CÓDIGO INVÁLIDO!\n')
    else:
        print('-' * 40)
        print(f'Informações do jogador {lista_jogadores[cod]["nome"]}')
        for i, g in enumerate(lista_jogadores[cod]["gols"]):
            print(f'-- Na {i+1}ª partida fez {g} gols.')
        print('-' * 40)
