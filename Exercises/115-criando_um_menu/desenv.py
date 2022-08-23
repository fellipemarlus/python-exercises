from lib import interface
from lib import arquivo
from time import sleep


arq = 'cursoemvideo.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.titulo('Saindo do sistema ...')
        break
    else:
        print('Erro, opção inválida!!')
    sleep(2)
