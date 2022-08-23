def contador(i, f, p):
    from time import sleep
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont -= p
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('~' * 30)
print("Contagem Personalizada!")
inicio = int(input('Digite o início da contagem: '))
fim = int(input('Digite o fim da contagem: '))
passo = int(input('Digite o passo da contagem: '))
contador(inicio, fim, passo)
print('Fim do programa!')
