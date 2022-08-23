# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

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

print(f'Foram digitados {len(numeros)} números.')
print(f'Lista de números em ordem crescente: {sorted(numeros)}')
print(f'Lista de números em ordem decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O número 5 está dentro da lista de números.')
else:
    print('O número 5 não está dentro da lista de números')

