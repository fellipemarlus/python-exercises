# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
from time import sleep

lista_pessoas = list()
mulheres = list()
soma = media = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input("Digite o nome da pessoa: ")).strip().title()
    while True:
        sexo = str(input("Digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
        if sexo in 'MmFf':
            pessoa['sexo'] = sexo
            if pessoa['sexo'] == 'F':
                mulheres.append(pessoa['nome'])
            break
        print('OPÇÃO INVALIDA! Digite apenas M (Masculino) ou F (Feminino).')
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    soma += pessoa['idade']
    lista_pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Quer adicionar dados de outra pessoa ? [S/N]: ')).strip().upper()[0]
        if continuar in "SN":
            break
        print('OPÇÃO INVALIDA! Digite apenas S (Sim) ou N (Não).')
    if continuar == 'N':
        break
media = soma / len(lista_pessoas)
print('\nCadastro finalizado!!')
print('Processando informações...')
sleep(2)
print(f'\nForam cadastradas {len(lista_pessoas)} pessoas.'), sleep(2)
print(f'A média de idade das pessoas cadastradas, são de {media:.2f} anos.'), sleep(2)
print(f'As mulheres cadastradas foram {mulheres}.'), sleep(2)
print('-' * 50)
print(f'As pessoas que estão com a idade acima da média:'), sleep(1)
for p in lista_pessoas:
    if p['idade'] >= media:
        print(f'{p["nome"]} com {p["idade"]} anos.'), sleep(2)
print('FIM DO PROGRAMA !!')
