# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input("Insira o valor do preço do produto desejado, para aplicarmos o desconto: "))
print("O novo preço com o desconto aplicado é de {} reais.".format(preço * (95/100)))