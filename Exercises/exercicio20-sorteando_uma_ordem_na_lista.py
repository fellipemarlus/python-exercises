# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample
print('Vamos sortear a ordem dos alunos para a apresentação do trabalho!')

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
alunos_f = (', '.join(sample(alunos, k=4)))

print(f'A ordem dos alunos para a apresentação é {alunos_f}')

