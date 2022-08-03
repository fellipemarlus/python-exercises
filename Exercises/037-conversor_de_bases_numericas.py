# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print("\nPrograma para conversão de números decimais para binário, octal ou hexadecimal.")

n = int(input('Digite o número que você quer que seja convertido: '))
print(f'\nAgora, digite a opção para a conversão do número:'
      f'\n(1) Para converter para número binário'
      f'\n(2) Para converter para número octal'
      f'\n(3) Para converter para número hexadecimal')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print(f'\nVocê escolheu converter para número binário.'
          f'\nO número {n} convertido para número binário é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'\nVocê escolheu converter para número octal.'
          f'\nO número {n} convertido para número octal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'\nVocê escolheu converter para número hexadecimal.'
          f'\nO número {n} convertido para número hexadecimal é igual a {hex(n)[2:]}')
else:
    print("Você escolheu uma opção inválida. Tente novamente")