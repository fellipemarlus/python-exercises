# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida. Digite o seu sexo corretamente (M/F): ')).strip().upper()[0]
print(f'O seu sexo é {sexo}')
