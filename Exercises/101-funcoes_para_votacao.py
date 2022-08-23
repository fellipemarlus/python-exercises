#  Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
#  o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
#  NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nascimento):
    import datetime
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - nascimento
    if 18 <= idade < 65:
        print(f'Você tem {idade} anos, seu voto é OBRIGATÓRIO!')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Você tem {idade} anos, e seu voto é OPCIONAL!')
    else:
        print(f'Você tem {idade} anos, e não pode votar ainda.')


ano = int(input('Digite o ano que você nasceu: '))
voto(ano)
print('~' * 40)
voto(1950)
