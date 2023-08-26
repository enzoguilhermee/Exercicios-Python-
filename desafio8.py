# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = int(input("Quantos metros são?: "))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print(" Isso equivale a:\n {} quilômetros.\n {} hectômetros.\n {} decâmetros.\n {} decímetros.\n {} centrímetros.\n {} milímetros.".format(km,hm,dam,dm,cm,mm))