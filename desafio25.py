'''Faça um programa que leia uma frase pelo teclado e mostre: 
Quantas vezes aparece a letra "A".
Em que posição ela aparece pela primeira vez.
Em que posição ela aparece pela última vez.'''
frase = str(input("Insira sua frase: ")).upper()
print("A letra (A) aparece {} vezes.".format(frase.count('A')))
print("A Primeira letra A apareceu na posição {}.".format(frase.find('A') + 1))
print("A última letra A apareceu na posição {}".format(frase.rfind('A') + 1))
