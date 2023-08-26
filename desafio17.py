'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
Calcule e mostre o comprimento da hipotenusa''' 
import math 
CA = float(input("Insira o valor do cateto adjacente: "))
CO = float(input("Insira o valor do cateto oposto: "))
HIP = math.sqrt(CA**2 + CO**2)

print("O valor do cateto adjacente é {:.2f}, o valor do cateto oposto é {:.2f} e o valor da hipotenusa é {:.2f}.".format(CA,CO,HIP))