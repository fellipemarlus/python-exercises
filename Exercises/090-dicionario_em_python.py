# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['media'] > 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k.upper()} é igual a {v}')


