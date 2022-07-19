# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.

velocidade = float(input('Informe a velocidade atual do seu carro: '))

if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print(f'\nVocê foi multado, por exceder o limite máximo permitido de 80KM/h.\n'
          f'Por estar {velocidade-80}KM/h acima da velocidade permitida\n'
          f'O valor da sua multa é R${multa:.2f}.')
else:
    print('\nVocê está dentro do limite permitido, uma boa viagem.')

