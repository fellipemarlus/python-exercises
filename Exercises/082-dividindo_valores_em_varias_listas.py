lista_princ = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in lista_princ:
        lista_princ.append(n)
    else:
        print('Você digitou um número repetido. Adicione outro.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer adicionar mais números? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

lista_par = []
lista_impar = []

for n in lista_princ:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

print(f'\nOs números digitados são: {lista_princ}')
print(f'Os números pares entre os números digitados são: {sorted(lista_par)}')
print(f'Os números impares entre os números digitados são: {sorted(lista_impar)}')