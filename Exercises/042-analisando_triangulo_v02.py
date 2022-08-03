# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('Vamos analisar se com as medidas informadas, podemos montar um triângulo e o seu tipo')
l1 = float(input('Digite a primeira medida: '))
l2 = float(input('Digite a segunda medida: '))
l3 = float(input('Digite a terceira medida: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com as medidas informadas, é possivel montar um triângulo.')
    if l1 == l2 and l2 == l3:
        print('O triângulo é do tipo EQUILÁTERO')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triângulo é do tipo ESCALENO')
    else:
        print('O triângulo é do tipo ISÓSCELES')
else:
    print('Com as medidas informadas, não é possível montar um triângulo.')

