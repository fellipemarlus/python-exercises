# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome_c = str(input('Digite o seu nome completo: '))
nome_d = nome_c.split() # Cria uma lista com os nomes separados

print(f'O seu nome com todas as letras maiusculas: {nome_c.upper()}')
print(f'O seu nome com todas as letras minusculas: {nome_c.lower()}')
print(f'O seu nome todo tem {len(nome_c.replace(" ",""))} letras') # método que retira os espaços da frase, e faz a contagem
print(f'O seu primeiro nome é {nome_d[0]} que tem {len(nome_d[0])} letras') # verifica o tamanho de cada nome, conforme o indice da lista
