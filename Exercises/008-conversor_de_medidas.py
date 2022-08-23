# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Vamos converter sua metragem !!')
metros = float(input('Digite a metragem que será convertida em centímetros e milímetros: '))
cm_metros = metros * 100
mm_metros = metros * 1000

print(f'O valor da metragem digitada foi {metros} M\nEsse valor convertido para centímetros é: {cm_metros:.0f} cm\n'
      f'O valor convertido para milímetros é: {mm_metros:.0f} mm')
