# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lis_palavras = ('agua', 'fogo', 'terra', 'ar', 'aumento', 'alimento')

a = e = i = o = u = ''
palavra = 0

for palavra in lis_palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

