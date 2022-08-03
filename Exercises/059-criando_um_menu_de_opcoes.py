# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print('Este programa serve para ler dois números,\n'
      'e o usuário após isso, escolherá o que fazer conforme o MENU de opções.\n')

print('Carregando programa leitor de números e opções do MENU ', end='')
print('.', end=''), sleep(1)
print('.', end=''), sleep(1)
print('.', end=''), sleep(1)
print('.\n', end=''), sleep(1)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('|-----------------------------------|\n'
          '|----------MENU DE OPÇÕES-----------|\n'
          '|-----------------------------------|\n'
          '|- [1] - Somar                      |\n'
          '|- [2] - Multiplicar                |\n'
          '|- [3] - Comparar qual é o maior    |\n'
          '|- [4] - Novos números              |\n'
          '|- [5] - Sair do programa           |\n'
          '|-----------------------------------|')
    opcao = int(input('\nDigite a opção desejada: '))
    if opcao == 1:
        soma = n1 + n2
        print('Você optou por somar os números.')
        print(f'A soma do número {n1} com o número {n2} é igual a : {soma}.\n'), sleep(4)
    if opcao == 2:
        mult = n1 * n2
        print('Você optou por multiplicar os números.')
        print(f'A multiplicação do número {n1} com o número {n2} é igual a : {mult}.\n'), sleep(4)
    if opcao == 3:
        print('Você optou por comparar qual dos números é o maior')
        print(f'Comparando o número {n1} e o número {n2}, o {max(n1, n2)} é o maior número.\n'), sleep(4)
    if opcao == 4:
        print('Você optou escolher novos números')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if opcao not in (1, 2, 3, 4, 5):
        print('Opção inválida, tente novamente.'), sleep(2)

print('Você optou por encerrar o programa.\n'
      ' ------PROGRAMA ENCERRADO------')
