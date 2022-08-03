# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('Vamos calcular e mostrar os 10 primeiros termos de uma Progressão Aritmética')
pt = int(input('Para isso, preciso que você digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0
print('\nOs 10 primeiros termos da progressão, são: ')

while c < 10:
    print(f'{pt}', end='')
    print(' -> ' if c < 9 else '', end='')
    pt += razao
    c += 1
