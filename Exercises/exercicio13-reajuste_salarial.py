# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('Vamos te dar 15% de aumento no seu salário!')
salario = float(input('Digite o valor do seu salário atual: R$'))
aumento_s = salario * 15 / 100 # ou salario * 1.15
print(f'Com o salário de R${salario:.2f}, você terá um aumento de R${aumento_s:.2f}\nSeu novo salário é R${salario+aumento_s:.2f}')