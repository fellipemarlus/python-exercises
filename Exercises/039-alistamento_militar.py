# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
ano_nasc = int(input('Digite o ano que você nasceu: '))
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

if (ano_atual - ano_nasc) < 18:
    dif = 18 - (ano_atual - ano_nasc)
    print(f'Você não atingiu a idade para se alistar, faltam {dif} anos')
elif (ano_atual - ano_nasc) > 18:
    dif = (ano_atual - ano_nasc) - 18
    print(f'Você ultrapassou a idade para se alistar, ultrapassou {dif} anos')
else:
    print(f'ATENÇÃO !!!\nNo ano de {ano_atual} você completa 18 anos.\n'
          f'Procure um posto ou agende pelo site o serviço de alistamento militar!')
