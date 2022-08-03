# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

print('DETECTOR DE PALÍNDROMO\n'
      'Você irá digitar uma frase/palavra, e iremos retirar os espaços e conferir\n'
      'se a frase/palavra é um palíndromo ou não.\n'
      'OBS: DIGITAR FRASES OU PALAVRAS SEM ACENTOS\n')
frase = str(input("Digite sua frase\palavra: ")).replace(' ', '').upper()
fraseinv = ''

for letra in range(len(frase) - 1, -1, -1):
    fraseinv += frase[letra]

if frase == fraseinv:
    print('A frase/palavra que você digitou, é um palíndromo!')
    print(f'Frase digitada : {frase}')
    print(f'Frase de forma inversa: {fraseinv}')
else:
    print('A frase/palavra que você digitou, não é um palíndromo!')

