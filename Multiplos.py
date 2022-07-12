#Leia 2 valores inteiros (A e B). 
#Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

valor, valor2 = input().split(' ')

valor = int(valor)
valor2 = int(valor2)

if valor2 % valor == 0 or valor % valor2 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')    