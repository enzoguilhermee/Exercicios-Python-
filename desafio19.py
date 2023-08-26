'''Um professor quer sortear seus 4 alunos para apagar o quadro. Faça um programa que ajude ele
lendo os nomes dele e escrevendo o nome do escolhido.'''
import random 
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista_de_alunos = [n1,n2,n3,n4]
escolhido = random.choice(lista_de_alunos)
print("O aluno escolhido foi {}.".format(escolhido))

