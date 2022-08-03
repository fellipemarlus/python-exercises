# A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Digite o ano que você nasceu: '))
idade = ano_atual - ano_nasc

if idade <= 9:
   print(f'\nVocê tem {idade} anos, sua categoria é MIRIM')
elif idade <= 14:
    print(f'\nVocê tem {idade} anos, sua categoria é INFANTIL')
elif idade <= 19:
    print(f'\nVocê tem {idade} anos, sua categoria é JUNIOR')
elif idade <= 25:
    print(f'\nVocê tem {idade} anos, sua categoria é SENIOR')
else:
    print(f'\nVocê tem {idade} anos, sua categoria é MASTER')


