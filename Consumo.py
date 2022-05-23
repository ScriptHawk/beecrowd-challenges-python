#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

distanciaPercorrida = int(input())
totalCombustivel = float(input())

consumoMedio = distanciaPercorrida/totalCombustivel

print('%.3f km/l'%consumoMedio)