#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
#MaiorAB = (A+B+ABS(A-B))/2
#Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

A,B,C = input().split(" ")

A = int(A)
B = int(B)
C = int(C)

if A > B and A > C or A == B:
    maior = A
elif B > A and B > C:
    maior = B
else: 
    C > A and C > B 
    maior = C

print(maior,'eh o maior') 