# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

texto = input('Digite algo: ')
# Resposta mais simples
print(f'O tipo primitivo do valor digitado é {type(texto)}')
print(f'O texto é alfanumérico ? {texto.isalnum()}')
print('--------------------------------------------------')
# Resposta com if e else
if texto.isalnum():
    print('O valor é alfanumérico ? Sim, é alfanumérico.')
else:
    print('O valor é alfanumérico ? Não.')

if texto.isspace():
    print('O valor só tem espaços ? Sim, só tem espaços.')
else:
    print('O valor só tem espaços ? Não.')

if texto.isnumeric():
    print('O valor é um número ? Sim, é um número.')
else:
    print('O valor é um número ? Não.')

if texto.isalpha():
    print('O valor é alfabético ? Sim, é alfabetico.')
else:
    print('O valor é alfabético ? Não.')

if texto.isupper():
    print('O valor está em letras maiúsculas ? Sim.')
else:
    print('O valor está em letras maiusculas ? Não.')
if texto.islower():
    print('O valor está em letras minusculas ? Sim.')
else:
    print('O valor está em letras minusculas ? Não.')
if texto.istitle():
    print('O valor está capitalizado ? Sim.')
else:
    print('O valor está capitalizado ? Não.')

print('''\nOBS: Um texto capitalizado é aquele em que todas as primeiras letras,
de cada palavra, estão em maiúsculo e o restante minúsculo.''')


