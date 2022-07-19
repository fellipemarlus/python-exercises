# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
print('Vamos sortear um dos quatro alunos presentes, para apagar o quadro!')

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]
alunos_f = (', '.join(alunos))

print(f'Alunos presentes na sala: {alunos_f}\nE o aluno escolhido para apagar o quadro foi ..... o {choice(alunos)}')