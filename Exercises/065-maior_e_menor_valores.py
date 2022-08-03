#  Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = cont = maior = menor = 0
opcao = ''
while opcao in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Você quer continuar ? [S]-Sim / [N]-Não ')).strip()[0]

media = soma / cont
print(f'A média dos valores digitados é {media:.2f}')
print(f'O maior valor foi o {maior}')
print(f'O menor valor foi o {menor}')



