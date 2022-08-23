
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

dados = {}
dados['nome'] = str(input('Digite seu nome: '))
dados['nascimento'] = int(input('Digite o ano de seu nascimento: '))
dados['ctps'] = int(input('Digite o número da sua carteira de trabalho: '))
dados['idade'] = ano_atual - dados['nascimento']
if dados['ctps'] > 0:
    dados['contratacao'] = int(input('Digite o ano em que você foi contratado: '))
    dados['salario'] = float(input('Digite o seu salário: R$'))
    dados['aposentadoria'] = 60 - dados['idade'] + 35

print('-' * 30)
print(f'\nSeu nome é {dados["nome"]}')
print(f'Você atualmente está com {dados["idade"]} anos.')
if dados['ctps'] > 0:
    print(f'Sua carteira de trabalho tem o nº {dados["ctps"]}')
    print(f'Seu salário é de R${dados["salario"]:.2f}')
    print(f'\nAs regras de aposentadoria são:\n'
          f'35 anos de contribuição e 60 anos de idade.\n'
          f'Se você continuar contribuindo com o INSS, você se aposentará com {dados["aposentadoria"]} anos')
