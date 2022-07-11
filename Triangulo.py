#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
#Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
#Perimetro = XX.X
#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:
#Area = XX.X

ladoA, ladoB, ladoC = input().split(' ')

ladoA = float(ladoA)
ladoB = float(ladoB)
ladoC = float(ladoC)

if (ladoA < (ladoB+ladoC)) and (ladoB < (ladoA+ladoC)) and (ladoC < (ladoB+ladoA)):
    perimetro = ladoA+ladoB+ladoC
    print('Perimetro = %.1f'%perimetro)
else:
    area = ((ladoA+ladoB)*ladoC)/2
    print('Area = %.1f'%area)        