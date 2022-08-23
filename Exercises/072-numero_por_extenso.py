numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte')

while True:
    indice = int(input('Digite um número entre 0 e 20: '))
    if indice in range(0, 21):
        print(f'Você digitou o número {numeros[indice]}.')
        break
