#Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
#As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

notas = int(input())
entrada = notas

notas100 = notas/100
notas100 = int(notas100)
notas = notas%100
notas50 = notas/50
notas50 = int(notas50)
notas = notas%50
notas20 = notas/20
notas20 = int(notas20)
notas = notas%20
notas10 = notas/10
notas10 = int(notas10)
notas = notas%10
notas5 = notas/5
notas5 = int(notas5)
notas = notas%5
notas2 = notas/2
notas2 = int(notas2)
notas = notas%2
notas1 = notas/1
notas1 = int(notas1)
notas = notas%1

print(entrada)
print(notas100,'nota(s) de R$ 100,00')
print(notas50,'nota(s) de R$ 50,00')
print(notas20,'nota(s) de R$ 20,00')
print(notas10,'nota(s) de R$ 10,00')
print(notas5,'nota(s) de R$ 5,00')
print(notas2,'nota(s) de R$ 2,00')
print(notas1,'nota(s) de R$ 1,00')
