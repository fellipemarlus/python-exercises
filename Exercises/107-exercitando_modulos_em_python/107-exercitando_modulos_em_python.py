# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input("Digite um valor: R$"))
print(f'A metade de R${valor:.2f} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor:.2f} é R${moeda.dobro(valor)}')
print()
porc = float(input("Digite uma porcentagem para ser calculado um acréscimo e diminuição no valor: % "))
print(f'O valor de R${valor:.2f} com acréscimo de {porc:.2f}%, é R${moeda.aumento(valor, porc)}')
print(f'O valor de R${valor:.2f} com diminuição de {porc:.2f}%, é R${moeda.diminuir(valor, porc)}')