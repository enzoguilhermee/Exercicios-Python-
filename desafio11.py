'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.'''
h = float(input("Qual a altura da parede que você deseja pintar?: "))
l = float(input("Qual a largura da parede que você deseja pintar?: "))
metros = h * l
print("Essa parede tem um total de {} metros quadrados e precisará de {} litros de tinta.".format(metros, metros/2))


