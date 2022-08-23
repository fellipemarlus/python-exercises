# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Você digitou um número repetido. Adicione outro.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer adicionar mais números? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\nOs números digitados e adicionados são: {sorted(numeros)}')
