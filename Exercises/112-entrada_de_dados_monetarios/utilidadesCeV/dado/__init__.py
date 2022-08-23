def leiaDinheiro(msg):
    import colorama
    from colorama import Fore
    colorama.init()
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{Fore.LIGHTRED_EX}ERRO: \'{entrada}\' é um preço inválido!{Fore.RESET}')
        else:
            valido = True
            return float(entrada)

