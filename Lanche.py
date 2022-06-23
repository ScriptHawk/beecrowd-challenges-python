#Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
#A seguir, calcule e mostre o valor da conta a pagar.
#Código 1 - Cachorro Quente - R$ 4.00
#Código 2 - X-Salada - R$ 4.50
#Código 3 - X-Bacon - R$ 5.00
#Código 4 - Torrada Simples - R$ 2.00
#Código 5 - Refrigerante - R$ 1.50

codigo, quantidade = input().split(' ')
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    valor = 4
elif codigo == 2:
    valor = 4.5
elif codigo == 3:
    valor = 5
elif codigo == 4:
    valor = 2
else: valor = 1.5

total = valor*quantidade

print('Total: R$ %.2f'%total)