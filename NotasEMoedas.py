#Leia um valor de ponto flutuante com duas casas decimais. 
#Este valor representa um valor monetário. 
#A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
#As notas consideradas são de 100, 50, 20, 10, 5, 2.
#As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
#A seguir mostre a relação de notas necessárias.

#Cria listas para notas e moedas
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

#Lê o valor
n = float(input())

print('NOTAS:')

#Divide o valor total pelo valor de cada nota
for nota in notas:
  qtd = int(round(n, 2) / nota)
#Tira o valor obtido acima
  n -= qtd * nota
#Imprime o resultado
  print('{} nota(s) de R$ {}.00'.format(qtd, nota))

print('MOEDAS:')

#Continua a operação com o valor restante
for moeda in moedas:
  qtd = int(round(n, 2) / moeda)
  n -= qtd * moeda
  print('{} moeda(s) de R$ {:.2f}'.format(qtd, moeda))