# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase qualquer: ").strip().lower()


print(f'A frase digitada foi: {frase}\n'
      f'Ela possui {frase.count("a")} letras "a"\n'
      f'A letra "a" aparece pela primeira vez na posicão nº {frase.find("a")+1}\n'
      f'A letra "a" aparece pela ultima vez na posição nº {frase.rfind("a")+1}')
