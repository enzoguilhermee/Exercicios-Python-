# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 
import random 
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista_de_alunos = [n1,n2,n3,n4]
escolhido = random.shuffle(lista_de_alunos)
print("A ordem de apresentação será:")
print(lista_de_alunos)