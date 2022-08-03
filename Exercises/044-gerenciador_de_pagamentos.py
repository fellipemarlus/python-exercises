# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

valor_p = float(input('Digite o valor do produto: R$ '))
print('\nAgora preciso que informe a forma de pagamento.'
      '\nConfira as opções abaixo:'
      '\n(1) Pagamento à vista'
      '\n(2) Pagamento com cartão de crédito')
opcao1 = int(input('Digite a opção de pagamento: '))
if opcao1 == 1:
    print('\nOk, o pagamento será à vista.'
          '\nOpções para pagamento à vista:'
          '\n(1) Dinheiro ou cheque. 10% de desconto'
          '\n(2) Cartao de débito.    5% de desconto')
    opcao2 = int(input('Digite a opção para pagamento à vista: '))
    if opcao2 == 1:
        print('\nO pagamento será em dinheiro/cheque e você terá 10% de desconto')
        print(f'Valor do produto R${valor_p:.2f} '
              f'\nValor para pagamento com 10% de desconto: R${valor_p - (valor_p * 10 / 100):.2f}')
    elif opcao2 == 2:
        print('\nO pagamento será com cartão de débito e você terá 5% de desconto')
        print(f'Valor do produto R${valor_p:.2f} '
              f'\nValor para pagamento com 5% de desconto: R${valor_p - (valor_p * 5 / 100):.2f}')
    else:
        print('Opção inválida, reinicie o programa')
elif opcao1 == 2:
    print('\nOk, o pagamento será com cartão de crédito.'
          '\nOpções de parcelamento para pagamentos com cartão de crédito:'
          '\n- Em até 2x. Sem desconto e sem juros'
          '\n- Entre 3x e 12x. 20% de juros')
    parcelas = int(input('Digite a quantidade de parcelas para pagamento com cartão de crédito: '))
    if parcelas < 2:
        mens = valor_p / parcelas
        print(f'\nO pagamento será em {parcelas}x no cartão de crédito, sem juros')
        print(f'O valor final ficará em R${valor_p:.2f} com parcelas de R${mens:.2f} por mês')
    elif parcelas <= 12:
        mens = (valor_p * 1.20) / parcelas
        print(f'\nO pagamento será em {parcelas}x no cartão de crédito, com 20% de juros')
        print(f'O valor final ficará em R${valor_p * 1.20:.2f} com parcelas de R${mens:.2f} por mês')
    else:
        print('Opção inválida, reinicie o programa')
else:
    print('Opção inválida, reinicie o programa')

