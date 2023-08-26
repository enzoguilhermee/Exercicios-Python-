'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.'''

velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print(" Você ultrapassou o limite de velocidade de 80km/h estando em {}km/h.\n Portanto, você foi multado e deverá pagar R${},00".format(velocidade,(velocidade - 80)*7))
else:
    print("Parabéns, você está dentro do limite de velocidade, continue assim!")