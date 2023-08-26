'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
quantos Dólares ela pode comprar.
Observação: Considere U$ 1 = R$ 3,27 '''
reais = float(input("Sem querer ser muito curioso, quantos reais você tem na carteira?: "))
print("Opa! Bastante grana, hein!? Com isso tudo na carteira você pode ter {:.2f} dólares. '0'".format(reais/3.27))
