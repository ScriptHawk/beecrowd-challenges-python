#Leia 3 valores inteiros e ordene-os em ordem crescente.
#No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

numero1,numero2,numero3 = input().split(' ')

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)

if numero1 < numero2 and numero2 < numero3 and numero1 < numero3:
    print(numero1)
    print(numero2)
    print(numero3)
    print('')
    print(numero1)
    print(numero2)
    print(numero3)
elif numero1 < numero3 and numero3 < numero2 and numero2 > numero1:
    print(numero1)
    print(numero3)
    print(numero2)
    print('')
    print(numero1)
    print(numero2)
    print(numero3)     
elif numero2 < numero1 and numero1 < numero3 and numero2 < numero3:
    print(numero2)
    print(numero1)
    print(numero3)
    print('')
    print(numero1)
    print(numero2)
    print(numero3)
elif numero2 < numero3 and numero3 < numero1 and numero2 < numero1:
    print(numero2)
    print(numero3)   
    print(numero1)
    print('')
    print(numero1)
    print(numero2)
    print(numero3)
elif numero3 < numero2 and numero2 < numero1 and numero3 < numero1:
    print(numero3)
    print(numero2)
    print(numero1)
    print('')
    print(numero1)
    print(numero2)
    print(numero3)
else:
    print(numero3)
    print(numero1)
    print(numero2)
    print('')
    print(numero1)
    print(numero2)
    print(numero3)

#Exemplo de ordem crescente usando Vetor
'''numeros = list(range(3)) 
for i in numeros:
    numeros[i] = int(input())
numeros.sort(key=int)
print(numeros)'''  