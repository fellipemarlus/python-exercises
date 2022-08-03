# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

numero = int(input('Digite um número: '))
print('A tabuada de {} é: '.format(numero))

for i in range(1, 11):
    tabuada = i * numero
    print(f'{numero} x {i} = {tabuada}')
