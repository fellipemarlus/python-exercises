# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda

valor = float(input("Digite um valor: R$"))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, format=True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, format=True)}')
print()
porc = float(input("Digite uma porcentagem para ser calculado um acréscimo e diminuição no valor: % "))
print(f'O valor de {moeda.moeda(valor)} com acréscimo de {porc:.2f}%, é {moeda.aumento(valor, porc, format=True)}')
print(f'O valor de {moeda.moeda(valor)} com diminuição de {porc:.2f}%, é {moeda.diminuir(valor, porc, format=True)}')