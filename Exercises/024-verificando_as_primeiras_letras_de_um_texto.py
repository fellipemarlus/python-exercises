# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome_cidade = input('Digite o nome da sua cidade: ').strip().upper().split()

if nome_cidade[0] == "SANTO":
    print('O nome da sua cidade começa com o nome "Santo"')
else:
    print('O nome da sua cidade não começa com o nome "Santo"')


'''nome_cidade = input('Digite o nome da sua cidade: ').strip().upper()
print(nome_cidade[:5] == "SANTO")'''
