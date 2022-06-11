#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

import math

A,B,C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)

B2 = math.pow(B, 2)
resultC = 4*A*C
divisor = 2*A
delta = B2-resultC

#verifica se o delta é maior que 0
if delta > 0:
 #verifica se a raiz quadrada de delta é maior que o 0    
 raizQuadrada = math.sqrt(delta)
 if raizQuadrada > 0 and divisor > 0 :
    R = (-(B)+raizQuadrada)/divisor
    R2= (-(B)-raizQuadrada)/divisor 
    print('R1 = {:.5f}'.format(R))
    print('R2 = {:.5f}'.format(R2))
 else:
    print('Impossivel calcular')
else:
    print('Impossivel calcular')
    
    
    

        
  


        
