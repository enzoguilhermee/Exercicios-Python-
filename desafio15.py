'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia 
e R$0,15 por Km rodado.'''
km = float(input("Quantos quilômetros percorridos tem seu carro alugado?: "))
dias = int(input("Por quantos dias você alugou o carro?: "))
pdias = dias * 60
pkm = km * 0.15
total = pdias + pkm
print(" Você alugou o carro por {} dias\n Andou com ele por {} quilômetros\n O preço total a se pagar das diárias do seu carro é {} reais\n O preço a se pagar por quilômetro percorrido é {} reais\n O total valor a se pagar é {} reais.".format(dias,km,pdias,pkm,total))
