# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

def sorteia(lista):
    from random import randint
    from time import sleep
    cont = 0
    print('Sorteando os números para a lista: ', end=''), sleep(0.5)

    while True:
        num = randint(0, 100)
        if num not in lista:
            lista.append(num)
            cont += 1
            print(f'{num} ', end=''), sleep(1)
        if cont >= 5:
            cont = 0
            break
    print()
    print('~' * 50)


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares entre {lista}, temos o resultado de {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)
