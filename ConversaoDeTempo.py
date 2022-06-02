#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

segundos = int(input())

minutos = segundos/60
segundosResto = segundos%60
minutos = int(minutos)
horas = minutos/60
minutosResto = minutos%60
horas = int(horas)
horasResto = horas%60

print(str(horasResto)+str(':')+str(minutosResto)+str(':')+str(segundosResto))