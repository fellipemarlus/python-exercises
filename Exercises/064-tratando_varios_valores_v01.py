# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Vamos somar os valores digitados, e contar quantos valores foram digitados.')
print('Para sair do programa, digite o número 999.')
cont = 0
soma = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print(f'Você digitou {cont} números, e a soma total desses valores digitados é {soma}')
