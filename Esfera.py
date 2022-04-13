#Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). 
#A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.

import math

raio = float(input())

volume = (4/3)*math.pi*(raio**3)

print('VOLUME = %.3f'%volume)