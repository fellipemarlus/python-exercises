# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moeda

valor = float(input("Digite um valor: R$"))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print()
porc = float(input("Digite uma porcentagem para ser calculado um acréscimo e diminuição no valor: % "))
print(f'O valor de {moeda.moeda(valor)} com acréscimo de {porc:.2f}%, é {moeda.moeda(moeda.aumento(valor, porc))}')
print(f'O valor de {moeda.moeda(valor)} com diminuição de {porc:.2f}%, é {moeda.moeda(moeda.diminuir(valor, porc))}')