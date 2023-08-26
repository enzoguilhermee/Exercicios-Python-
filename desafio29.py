'''Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
num = int(input("Insira um númeiro inteiro qualquer: "))
if num % 2 == 0:
    print("O número que você escolheu foi {} e ele é um número par.".format(num))
else:
    print("O número que você escolheu foi {} e ele é um número ímpar.".format(num))