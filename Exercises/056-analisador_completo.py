# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.
soma_idade = 0
m_idade = 0
mulher_20 = 0
h_velho = ''
for i in range(1, 5):
    nome = str(input(f'\nDigite o nome da {i}ª pessoa: ')).title()
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}ª pessoa: (M OU F) - ')).strip().upper()
    if idade > m_idade and sexo == 'M':
        m_idade = idade
        h_velho = nome
        soma_idade += idade
    else:
        if sexo == 'F' and idade < 20:
            soma_idade += idade
            mulher_20 += 1
        else:
            soma_idade += idade

media_idade = soma_idade / 4
print(f'\nO homem mais velho é o {h_velho}')
print(f'A média de idade é de {media_idade} anos')
print(f'Considerando os registros, existem {mulher_20} mulheres com menos de 20 anos.')
