#Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados.
#A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
#Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
#Se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
#Se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
#Se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
#Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
#Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

import math

ladoA, ladoB, ladoC = input().split(' ')

ladoA = float(ladoA)
ladoB = float(ladoB)
ladoC = float(ladoC)

if ladoA >= ladoB and ladoB >= ladoC and ladoA >= ladoC:
    maior = ladoA
    doMeio = ladoB
    menor = ladoC
elif ladoA >= ladoB and ladoC >= ladoB and ladoA >= ladoC:
    maior = ladoA
    doMeio = ladoC
    menor = ladoB   
elif ladoB >= ladoA and ladoB >= ladoC and ladoA >= ladoC:
    maior = ladoB
    doMeio = ladoA
    menor = ladoC
elif ladoB >= ladoA and ladoB >= ladoC and ladoC >= ladoA:
    maior = ladoB
    doMeio = ladoC
    menor = ladoA
elif ladoC >= ladoA and ladoC >= ladoB and ladoB >= ladoA:
    maior = ladoC
    doMeio = ladoB
    menor = ladoA
elif ladoC >= ladoA and ladoC >= ladoB and ladoA >= ladoB:
    maior = ladoC
    doMeio = ladoA
    menor = ladoB  

if maior >= doMeio+menor:
    print('NAO FORMA TRIANGULO')
elif math.pow(maior,2) == math.pow(doMeio,2)+math.pow(menor,2):
    print('TRIANGULO RETANGULO')
elif math.pow(maior,2) > math.pow(doMeio,2)+math.pow(menor,2):
    print('TRIANGULO OBTUSANGULO')
elif math.pow(maior,2) < math.pow(doMeio,2)+math.pow(menor,2):
    print('TRIANGULO ACUTANGULO')

if maior == doMeio and doMeio == menor and maior == menor:
    print('TRIANGULO EQUILATERO')
elif maior == doMeio or maior == menor or doMeio == menor:
    print('TRIANGULO ISOSCELES')