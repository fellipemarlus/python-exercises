# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('Calculadora de preço de viagem.')
distancia = float(input("Digite a distância da sua viagem, em KM: "))

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

# valor = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(f'O valor da sua viagem de {distancia:.1f}KM, ficará R${valor:.2f} ')
