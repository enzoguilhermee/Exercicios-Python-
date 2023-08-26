'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random 
lista = [0,1,2,3,4,5]
aleatory = random.choice(lista)
num = int(input("Escolha um número de 0 a 5: "))
if num == aleatory:
    print("Parabéns! Você adivinhou o número que o computador pensou.")
else:
    print("Que pena! O número escolhido pelo computador foi {} e o seu foi {}. Mais sorte da próxima vez!".format(aleatory,num))