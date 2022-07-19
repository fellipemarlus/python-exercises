# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

# Realizei inicialmente com o laço for por achar mais prático.
'''numero = int(input('Digite um número: '))
print('A tabuada de {} é: '.format(numero))

for i in range(1, 11):
    tabuada = i * numero
    print(f'{numero} x {i} = {tabuada}')'''

# Tentei realizar como se não soubesse usar o laço for
# Formatação confome vi na vídeo aula

numero = int(input('Digite um número: '))
print('_'*15)
print(f'A tabuada de {numero}:')
print(f'{numero} x {1:2} = {numero * 1}')
print(f'{numero} x {2:2} = {numero * 2}')
print(f'{numero} x {3:2} = {numero * 3}')
print(f'{numero} x {4:2} = {numero * 4}')
print(f'{numero} x {5:2} = {numero * 5}')
print(f'{numero} x {6:2} = {numero * 6}')
print(f'{numero} x {7:2} = {numero * 7}')
print(f'{numero} x {8:2} = {numero * 8}')
print(f'{numero} x {9:2} = {numero * 9}')
print(f'{numero} x {10:2} = {numero * 10}')
print('_'*15)
