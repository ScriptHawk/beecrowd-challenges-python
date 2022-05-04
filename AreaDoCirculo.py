#A fórmula para calcular a área de uma circunferência é: area = π . raio2. 
#Considerando para este problema que π = 3.141592:
#Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

import math
#n = 3.141592
raio = float(input())
area = math.pi*(raio**2)

print('A=%.4f'%area)