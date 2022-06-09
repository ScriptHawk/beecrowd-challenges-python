#Leia 4 valores inteiros A, B, C e D.
#A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos
#e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

A,B,C,D = input().split(' ')

#Conversão das váriaveis em inteiras 
A = int(A)
B = int(B)
C = int(C)
D = int(D)
#Variáveis E e F criadas para facilitar a comparação de soma
E = C+D
F = A+B

if B > C and D > A and E > F and C >= 0 and D >= 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')