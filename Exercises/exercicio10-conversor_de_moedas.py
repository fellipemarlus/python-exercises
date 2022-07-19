# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
# pode comprar.

saldo_rs = float(input('Digite o saldo que você tem em carteira: '))
saldo_usd = saldo_rs / 5.43

print(f'Com o valor de R${saldo_rs:.2f}, você pode comprar {round(saldo_usd):.2f} dólares.'
      f'\nHOJE, 1$ Dólar equivale a 5 Reais e 43 centavos. R$5,43')