#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#  de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Vamos calular o preço final do aluguel do veículo.')
dias = float(input('Quantos dias o carro ficou com o cliente ?'))
km_rodado = float(input('Digite quantos KM, o cliente percorreu: '))
print('A base de preço é:\n'
      'R$60,00 ---- por dia de aluguel\n'
      'R$0,15 ----- por KM rodado\n')

pag = (dias * 60) + (km_rodado * 0.15)
print(f'O cliente rodou {km_rodado:.2f}KM, e usou o veículo por {dias:.0f} dias.\n'
      f'O preço final do aluguel é de R${pag:.2f}')


