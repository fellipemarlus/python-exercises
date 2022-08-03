# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Vamos calcular e mostrar inicialmente,\n'
      'os 10 primeiros termos de uma Progressão Aritmética,\n'
      'você terá a opção de ver mais termos, e poderá parar quando digitar 0.\n')
pt = int(input('Para isso, preciso que você digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0
total = 0
mais = 10
print('\nOs 10 primeiros termos da progressão, são: ')


while mais != 0:
    total = total + mais
    while c < total:
        print(f'{pt} -> ', end='')
        pt += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Programa encerrado!')

