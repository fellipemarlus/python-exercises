# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = [int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')),
           int(input('Digite o quinto número: '))]

maior = max(numeros)
menor = min(numeros)
print(f'Você digitou os números {numeros}')

print(f'O maior número da lista é o {maior} que está na posição ', end='')
for i, n in enumerate(numeros):
    if n == maior:
        print(f'{i}...', end='')
print(f'\nO menor número da lista é o {menor} que está na posição ', end='')
for i, n in enumerate(numeros):
    if n == menor:
        print(f'{i}...', end='')




#e o menor número da lista é o {menor}, que estão nos índices'
 #     f' {numeros.index(maior)} e {numeros.index(menor)}, respectivamente.')


'''numeros = []
maior = 0
menor = 0
for c in range(0, 5):
    numeros.append(int(input('Digite um valor para a posição {c}: ))
    if c == 0:
    maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
        maior = numeros[c]
        if numeros[c] < menor:
        menor = numeros[c]
print('-' * 30)'''


