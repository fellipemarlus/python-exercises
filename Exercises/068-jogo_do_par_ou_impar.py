# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0
print('----------Jogo do Par ou Ímpar---------')
print('Se você perder, o jogo é finalizado.\n')
while True:
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('Escolha se quer jogar Par ou Ímpar ? [P/I]: ')).strip().upper()[0]
    usuario = int(input('Digite o número que você jogará: '))
    comp = randint(0, 10)
    resultado = usuario + comp

    if jogada in 'Pp' and resultado % 2 == 0:
        print(f'\nVocê venceu, o resultado foi {resultado} e deu par.')
        print(f'Sua jogada foi {usuario} e a do computador foi {comp}\n')
        vitorias += 1
    if jogada in 'Pp' and resultado % 2 == 1:
        print(f'\nVocê perdeu, o resultado foi {resultado} e deu impar')
        print(f'Sua jogada foi {usuario} e a do computador foi {comp}\n')
        break
    if jogada in 'Ii' and resultado % 2 == 1:
        print(f'\nVocê venceu, o resultado foi {resultado} e deu ímpar.')
        print(f'Sua jogada foi {usuario} e a do computador foi {comp}\n')
        vitorias += 1
    if jogada in 'Ii' and resultado % 2 == 0:
        print(f'\nVocê perdeu, o resultado foi {resultado} e deu par.')
        print(f'Sua jogada foi {usuario} e a do computador foi {comp}\n')
        break

print(f'Você conseguiu {vitorias} vitórias consecutivas !!')

# Fiz em 43 minutos
