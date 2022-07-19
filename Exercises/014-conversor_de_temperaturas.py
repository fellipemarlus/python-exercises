# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('Vamos converter a temperatura em graus Celsius, para graus Fahrenheit')
c = float(input('Digite a temperatura em graus Celsius °C: '))
f = c * 1.8 + 32

print(f'A temperatura de {c:.1f} °C, é o mesmo que {f:.1f} °F.')