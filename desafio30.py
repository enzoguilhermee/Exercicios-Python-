'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 
para viagens mais longas.'''
km = int(input("Insira quantos km foi sua viagem: "))
if km <= 200:
    print("Você andou {}km e sua viagem custou R${}.".format(km,km*0.5))
else:
    print("Você andou {}km e sua viagem custou R${}".format(km,km*0.45))