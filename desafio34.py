'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuários se elas podem ou não 
formar um triangulo.'''
r1 = int(input("Insira o comprimento da reta 1: "))
r2 = int(input("Insira o comprimento da reta 2: "))
r3 = int(input("Insira o comprimento da reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: 
    print("Essas retas podem formar um triângulo.")
else: 
    print("Essas retas não podem formar um triângulo.")