# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
import colorama
from colorama import Fore
colorama.init()
print('Vamos calcular o aumento do seu salário!')
salario = float(input('Digite o seu salário: R$'))
if salario <= 1250:
    aumento = salario * 15 / 100
else:
    aumento = salario * 10 / 100

print(f'O seu novo salário é {Fore.GREEN}R${salario+aumento:.2f}{Fore.RESET} após um aumento de R${aumento:.2f}')