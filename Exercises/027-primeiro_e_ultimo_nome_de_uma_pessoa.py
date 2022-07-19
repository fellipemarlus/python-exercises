# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip().split()
print(f'O seu primeiro nome é {nome[0]}\n'
      f'O seu ultimo nome é {nome[-1]}')
