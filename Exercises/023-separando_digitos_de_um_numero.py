#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número inteiro, entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Você digitou o numero {numero}\n'
      f'Milhar : {m}\n'
      f'Centena: {c}\n'
      f'Dezena: {d}\n'
      f'Unidade: {u}\n')
