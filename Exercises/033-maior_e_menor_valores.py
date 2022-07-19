# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite três números, e informarei qual dos três números é o maior, e qual é o menor.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
print(f'\nO maior número digitado foi o {maior}')

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor número digitado foi o {menor}')

# print(f'O maior número digitado foi o {max(n1, n2, n3)}')
# print(f'O menor número digitado foi o {min(n1, n2, n3)}')

