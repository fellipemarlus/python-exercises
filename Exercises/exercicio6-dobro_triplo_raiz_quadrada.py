# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número, para ser calculado o seu dobro, triplo e a sua raiz quadrada: "))

print(f'Número digitado: {n}\nDobro do número digitado: {n*2}\nTriplo do número digitado: {n*3}\n'
      f'Raiz quadrada do número digitado: {n**(1/2):.2f}')