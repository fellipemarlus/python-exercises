# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year

print(ano_atual)
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    if (ano_atual - ano) >= 18:
        maior += 1
    else:
        menor += 1
print(f'Conforme o ano de nascimento das 7 pessoas informadas\n'
      f'Temos {maior} pessoas que são maiores de idade e {menor} pessoas que são menores de idade')

