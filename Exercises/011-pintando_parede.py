# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta
# uma área de 2 metros quadrados.

print('Vamos calcular a quantidade de tinta necessária para pintar paredes.\n')
altura = float(input('Digite a altura (em metros) da parede que será pintada: '))
largura = float(input('Digite a largura (em metros) da parede que será pintada: '))
area = altura * largura
qt_tinta = area * 0.5

print(f'A sua parede tem a área de {area}m²')
print(f'Com isso será necessário {qt_tinta} Litros de tinta para pintar toda a parede.')