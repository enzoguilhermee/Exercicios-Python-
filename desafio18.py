#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente do angulo.
from math import sin, cos, tan, degrees 
angulo = int(input("Insira o valor dos ângulos: "))

print("O seno do ângulo em radianos é {:.3f}, o cosseno do ângulo em radianos é {:.3f} e a tangente do ângulo em radianos é {:.3f}.".format(sin(angulo),cos(angulo),tan(angulo)))
print("O seno do ângulo em radianos é {:.1f}, o cosseno do ângulo em radianos é {:.1f} e a tangente do ângulo em radianos é {:.1f}.".format(degrees(sin(angulo)),degrees(cos(angulo)),degrees(tan(angulo))))
