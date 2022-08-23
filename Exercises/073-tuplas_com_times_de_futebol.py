# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
#
# d) Em que posição está o time do Botafogo.

t_camp_brasileiro = ('Inicio', 'Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR',
                     'Flamengo', 'Internacional', 'Atlético-MG', 'Bragantino', 'Santos',
                     'São Paulo', 'Goiás', 'Botafogo', 'América-MG', 'Ceará', 'Coritiba',
                     'Avaí', 'Cuiabá', 'Fortaleza', 'Atlético-GO', 'Juventude')

'''print(len(t_camp_brasileiro))
print(t_camp_brasileiro[1:6])
print(t_camp_brasileiro[16:])
print(sorted(t_camp_brasileiro))
print([t_camp_brasileiro.index('Botafogo')])'''

cont_p = 1
print('Os 5 primeiros times na tabela do Campeonato Brasileiro de 2022.\n'
      'Atualizado em 03/08/2022')
print('_' * 25)
for time in t_camp_brasileiro[1:6]:
    print(f'{cont_p}ª Posição - {time}')
    cont_p += 1
print('_' * 25)

cont_u = 17
print('Os 4 últimos times na tabela do Campeonato Brasileiro de 2022.\n'
      'Atualizado em 03/08/2022')
print('_' * 25)
for time in t_camp_brasileiro[17:]:
    print(f'{cont_u}ª Posição - {time}')
    cont_u += 1
print('_' * 25)

print('Times do Campeonato Brasileiro de 2022 organizados em ordem alfabética. ')
print(sorted(t_camp_brasileiro))
print('_' * 43)

pos_botafogo = t_camp_brasileiro.index('Botafogo')
print(f'O Botafogo atualmente está na {pos_botafogo}ª posição.')
print('_' * 43)
