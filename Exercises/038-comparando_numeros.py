# Escreva um programa que leia dois números inteiros e compare-os.
# Mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print('Vamos fazer a comparação de dois números inteiros!\n')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n2 > n1:
    print('O segundo número é maior.')
else:
    print('Não existe valor maior, os dois números são iguais.')

