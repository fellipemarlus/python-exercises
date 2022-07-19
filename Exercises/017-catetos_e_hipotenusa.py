# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# Forma sem usar o módulo Math
'''cat_oposto = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))

hipotenusa = (cat_oposto**2 + cat_adj**2) ** (0.5)
print(f'A hipotenusa deste triangulo retângulo é {hipotenusa:.2f}')'''


from math import hypot
cat_oposto = float(input('Digite o cateto oposto: '))
cat_adj = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adj)
print(f'A hipotenusa deste triangulo retângulo é {hipotenusa:.2f}')



