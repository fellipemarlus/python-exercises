# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("Vamos analisar se você pode pegar um empréstimo bancário para compra de uma casa")
print("Vamos começar com algumas perguntas!\n")

v_casa = float(input('Digite o valor da casa: R$'))
v_salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Informe em quantos anos você vai pagar: '))
limit_salario = v_salario * 30 / 100
mensalidade = v_casa / (anos * 12)

if mensalidade <= limit_salario:
    print('\nEmpréstimo aprovado!')
    print(f'O valor da prestação mensal ficará em R${mensalidade:.2f}')
else:
    print('\nEmpréstimo negado! Valores fora da regra estabelecida.')
    print('REGRA: A prestação mensal não pode exceder 30% do salário')



