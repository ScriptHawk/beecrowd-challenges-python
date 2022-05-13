#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nomeVendedor = str(input())
salarioFixo = float(input())
totalVendas = float(input())

totalVendas = totalVendas*0.15
salarioFixo = totalVendas+salarioFixo

print('TOTAL= R$ %.2f'%salarioFixo)