# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem
#com a data formatada.
dia = str(int(input("Insira o dia do seu nascimento: ")))
mes = str(input("Insira o mês do seu nascimento: "))
ano = str(int(input("Insira o ano do seu nascimento ")))

print("Que legal! Você nasceu no dia {} do mês {} de {} correto?".format(dia,mes,ano))