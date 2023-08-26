'''Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira'''
import math 
num = float(input("Insira um numero: "))
print("O valor digitado foi {} e a sua porção inteira é {}.".format(num, math.trunc(num)))
