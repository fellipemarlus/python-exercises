# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido. ]
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! digite um número real.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


ni = leiaInt("Digite um valor inteiro: ")
nf = leiaFloat("Digite um valor real: ")
print(f'O valor inteiro digitado foi {ni} e o valor real digitao foi {nf}.')
