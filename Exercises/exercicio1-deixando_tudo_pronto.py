#Crie um programa que escreva "Olá, mundo!" na tela.
import colorama
from colorama import Fore
colorama.init()

textoPtBr = "Olá, Mundo!"
textoEng = "Hello, World!"

print(f"{Fore.CYAN}Olá, Mundo!!!{Fore.RESET}")
print(textoPtBr)
print(textoEng)
