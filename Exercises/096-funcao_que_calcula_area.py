# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calc_area():
    print("Calculadora de área")
    print('-' * len("Calculadora de área"))
    larg = float(input("Digite a largura do terreno (M): "))
    comp = float(input("Digite o comprimento do terreno (M): "))
    print(f'Um terreno de {larg} x {comp}, tem uma área de {larg * comp}m².')


calc_area()


