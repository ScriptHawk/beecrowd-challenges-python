#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

#Área Triângulo Retângulo
areatriangulo = (A*C)/2

#Área Circulo
areacirculo = pi*(C**2)

#Área Trapézio
areatrapezio = ((A+B)/2)*C

#Área Quadrado
areaquadrado = B**2

#Área Retângulo
arearetangulo = A*B

print('TRIANGULO: %.3f'%areatriangulo)
print('CIRCULO: %.3f'%areacirculo)
print('TRAPEZIO: %.3f'%areatrapezio)
print('QUADRADO: %.3f'%areaquadrado)
print('RETANGULO: %.3f'%arearetangulo)