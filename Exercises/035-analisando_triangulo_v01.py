# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('Vamos analisar se com as medidas informadas, podemos montar um triângulo')
l1 = float(input('Digite o primeiro número: '))
l2 = float(input('Digite o segundo número: '))
l3 = float(input('Digite o terceiro número: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com as medidas informadas, é possivel montar um triângulo')
else:
    print('Com as medidas informadas, não é possível montar um triângulo')



