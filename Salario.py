#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. 
#A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

numeroFuncionario = int(input())
horasTrabalhadas = int(input())
valorHora = float(input())

salarioFinal = horasTrabalhadas*valorHora

print(str("NUMBER= ") + str(numeroFuncionario))
print('SALARY = U$ %.2f'%salarioFinal)