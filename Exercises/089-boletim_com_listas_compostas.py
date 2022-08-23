# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.

alunos = []
s = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    s += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Quer adicionar as notas de outro aluno? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 21)
print(f'{"Nº":<3} {"NOME":<10} {"MÉDIA":>5}')
print('-' * 21)

for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>5}')

while True:
    print('-' * 50)
    opcao = int(input('Você quer ver as notas de qual aluno ? [999 interrompe]: '))
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
    if opcao == 999:
        print('\nPrograma encerrado')
        break





