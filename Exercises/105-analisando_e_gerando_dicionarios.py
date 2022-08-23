# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*n, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, para saber a situação do aluno
    :return: dicionário com várias informações sobre a situação da turma
    """

    result = dict()
    result['total'] = len(n)
    result['maior'] = max(n)
    result['menor'] = min(n)
    result['media'] = sum(n) / len(n)
    if sit:
        if result['media'] >= 7:
            result['situacao'] = 'APROVADO'
        elif result['media'] >= 5:
            result['situacao'] = 'EM RECUPERAÇÃO'
        else:
            result['situacao'] = 'REPROVADO'
    return result


resp = notas(5, 8, 5, 6, sit=True)
print(resp)
print()
resp = notas(2, 4, 5, 6)
print(resp)
print()
resp = notas(9, 8, 6, 7, sit=True)
print(resp)
print()
help(notas)
