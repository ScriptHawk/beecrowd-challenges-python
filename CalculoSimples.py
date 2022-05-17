#Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
#Após, calcule e mostre o valor a ser pago.
#O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

#atribui os 3 valores inseridos em mesma linha e atribui as respectivas variáveis
codigoPeca, numeroPecas, valorUnitario = input().split(" ")
#converte as variáveis do input
codigoPeca = int(codigoPeca)
numeroPecas = int(numeroPecas)
valorUnitario = float(valorUnitario)

#refaz o processo de atribuir váriaveis inseridas em mesma linha
codigoPeca2, numeroPecas2, valorUnitario2 = input().split(" ")
codigoPeca2 = int(codigoPeca2)
numeroPecas2 = int(numeroPecas2)
valorUnitario2 = float(valorUnitario2)

peca1 = (numeroPecas*valorUnitario)
peca2 = (numeroPecas2*valorUnitario2)
total = peca1+peca2


print('VALOR A PAGAR:R$ %.2f'%total)