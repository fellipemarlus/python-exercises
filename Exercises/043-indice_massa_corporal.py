# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print('\nCALCULADORA DE IMC\n')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'\nSeu (IMC) está em {imc:.2f}.\nVocê está ABAIXO DO PESO.')
elif imc < 25:
    print(f'\nSeu (IMC) está em {imc:.2f}.\nVocê está no PESO IDEAL.')
elif imc < 30:
    print(f'\nSeu (IMC) está em {imc:.2f}.\nVocê está com SOBREPESO.')
elif imc < 40:
    print(f'\nSeu (IMC) está em {imc:.2f}.\nVocê está com OBESIDADE.')
else:
    print(f'\nSeu (IMC) está em {imc:.2f}.\nVocê está com OBESIDADE MÓRBIDA.')
