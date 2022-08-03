# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_i = homens = mulher_20 = 0
# seguir = 'S'
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior_i += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulher_20 += 1

    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Você quer adicionar mais dados? [S/N]: ')).strip().upper()[0]
        print('--------------------------------------------')
    if seguir == 'N':
        break

print(f'Analisando os dados informados, podemos dizer que:\n'
      f'- Temos {maior_i} pessoas que são maiores de idade\n'
      f'- Temos {homens} homens\n'
      f'- Temos {mulher_20} mulheres que tem menos de 20 anos.')

