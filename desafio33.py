'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00 calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15% '''

salario = float(input("Digite o salário do funcionário desejado: "))
if salario > 1250:
    print("O salário é de {} e teve um aumento de 10%, sendo agora de R${}.".format(salario, salario + (salario * (10/100))))
else:
    print("O salário é de {} e teve um aumento de 15%, sendo agora de R${}.".format(salario,salario + (salario * (15/100))))