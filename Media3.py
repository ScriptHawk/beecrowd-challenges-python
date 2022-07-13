#Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
#Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ".
#Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
#Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
#Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

N1, N2, N3, N4 = input().split(' ')

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

N1 = N1*2
N2 = N2*3
N3 = N3*4
N4 = N4*1 

media = (N1+N2+N3+N4)/10

if media >= 7:
    print("Media: %.1f"%media)
    print("Aluno aprovado.")
elif media < 5:
    print("Media: %.1f"%media)
    print("Aluno reprovado.")
elif media >=5 and media <= 6.9:
    print("Media: %.1f"%media)
    print('Aluno em exame.')
    notaExame = float(input())
    print('Nota do exame:',notaExame)
    mediaFinal = (media+notaExame)/2 
    if mediaFinal >=5:
     print('Aluno aprovado.')
     print('Media final: %.1f'%mediaFinal)
    elif mediaFinal <= 4.9:
     print('Aluno reprovado.')
     print('Media final: %.1f'%mediaFinal)   