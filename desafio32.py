'''Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.'''
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo núemro: "))
n3 = float(input("Insira o terceiro número: "))

if n1>n2>n3:
    print("O número maior é {} e o menor é {}.".format(n1,n3))
if n1>n3>n2:
    print("O número maior é {} e o menor é {}.".format(n1,n2))
if n2>n1>n3:
    print("O número maior é {} e o menor é {}.".format(n2,n3))
if n2>n3>n1:
    print("O número maior é {} e o menor é {}.".format(n2,n1))
if n3>n2>n1:
    print("O número maior é {} e o menor é {}.".format(n3,n1))
if n3>n1>n2:
    print("O número maior é {} e o menor é {}.".format(n3,n2))