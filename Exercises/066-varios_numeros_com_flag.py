# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

cont = soma = 0
while True:
    n = int(input('Digite um número inteiro: (999 Para sair)'))
    if n == 999:
        print('Você digitou o número 999 para sair.\n')
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números, e a soma deles é {soma}.')
