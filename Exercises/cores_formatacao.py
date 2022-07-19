import colorama
from colorama import Fore
from colorama import Style

colorama.init()
print(f'{Fore.BLUE}AZUL{Fore.RESET}')
print(f'{Fore.LIGHTBLUE_EX}LIGHT BLUE{Fore.RESET}')

print(f'{Fore.GREEN}VERDE{Fore.RESET}')
print(f'{Fore.LIGHTGREEN_EX}LIGHT GREEN{Fore.RESET}')

print(f'{Fore.RED}VERMELHO{Fore.RESET}')
print(f'{Fore.LIGHTRED_EX}LIGHT RED{Fore.RESET}')

print(f'{Fore.YELLOW}AMARELO{Fore.RESET}')
print(f'{Fore.LIGHTYELLOW_EX}LIGHT YELLOW EX{Fore.RESET}')

print(f'{Fore.BLACK}BLACK{Fore.RESET}')
print(f'{Fore.LIGHTBLACK_EX}LIGHT BLACK{Fore.RESET}')

print(f'{Fore.CYAN}CIANO{Fore.RESET}')
print(f'{Fore.LIGHTCYAN_EX}LIGHT CYAN{Fore.RESET}')

print(f'{Fore.MAGENTA}MAGENTA{Fore.RESET}')
print(f'{Fore.LIGHTMAGENTA_EX}LIGHT MAGENTA{Fore.RESET}')

print(f'{Fore.WHITE}WHITE{Fore.RESET}')
print(f'{Fore.LIGHTWHITE_EX}LIGHT WHITE{Fore.RESET}')

print()
print(f'{Style.BRIGHT}NEGRITO{Style.RESET_ALL}')
print(f'{Style.DIM}DIM{Style.RESET_ALL}')
print(f'{Style.NORMAL}NORMAL{Style.RESET_ALL}')
print(f'{Style.RESET_ALL}RESETA TUDO{Style.RESET_ALL}')