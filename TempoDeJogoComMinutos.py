#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo.
#A seguir calcule a duração do jogo.
#Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

horaJogo = horaFinal - horaInicial + 24 * int(horaFinal < horaInicial or 
(minutoFinal < minutoInicial and horaFinal <= horaInicial) or 
(horaFinal == horaInicial and minutoFinal == minutoInicial)) - int(minutoFinal < minutoInicial)
minutoJogo = minutoFinal - minutoInicial + 60 * int(minutoFinal < minutoInicial)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horaJogo, minutoJogo))

#código antigo
'''horaInicio, minutoInicio, horaFim, minutoFim = input().split(' ')
horaInicio = int(horaInicio)
minutoInicio = int(minutoInicio)
horaFim = int(horaFim)
minutoFim = int(minutoFim)

hora = 0
diferencaHora = 0
minuto = 0

if horaInicio > horaFim and minutoInicio == minutoFim:
    while horaInicio < 24:
        horaInicio = horaInicio+1
        hora = hora+1
    hora = hora+horaFim
    print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
elif horaInicio < horaFim and minutoInicio == minutoFim:
    hora = horaFim-horaInicio
    print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
elif horaInicio > horaFim and minutoInicio > minutoFim:
    while horaInicio < 24:
        horaInicio = horaInicio+1
        hora = hora+1
    hora = (hora+horaFim)-1
    while minutoInicio < 60:
        minutoInicio = minutoInicio+1
        minuto = minuto+1
    minuto = minuto+minutoFim
    print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
elif horaInicio > horaFim and minutoInicio < minutoFim:
    while horaInicio < 24:
        horaInicio = horaInicio+1
        hora = hora+1
    hora = hora+horaFim
    minuto = minutoFim-minutoInicio
    print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
elif horaFim > horaInicio and minutoFim > minutoInicio:
    if minutoFim >=60:
        minuto = minutoFim%60
        roundMinuto = minutoFim/60
        roundMinuto = int(roundMinuto)
        hora = horaFim+roundMinuto
        print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
    else:    
        hora = horaFim-horaInicio
        minuto = minutoFim-minutoInicio
        print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
elif horaFim > horaInicio and minutoInicio > minutoFim:
    while minutoInicio < 60:
        minutoInicio = minutoInicio+1
        minuto = minuto+1
    minuto = minuto+minutoFim
    while horaInicio < horaFim:
        horaInicio = horaInicio+1
        diferencaHora = diferencaHora+1
    diferencaHora = diferencaHora-1    
    print('O JOGOU DUROU %.0f HORA(S)'%diferencaHora,'E %.0f MINUTO(S)'%minuto)    
elif horaInicio == horaFim and minutoInicio > minutoFim:
    while horaInicio < 24:
        horaInicio = horaInicio+1
        hora = hora+1
    hora = (hora+horaFim)-1    
    while minutoInicio < 60:
        minutoInicio = minutoInicio+1
        minuto = minuto+1
    minuto = minuto+minutoFim    
    print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)    
elif horaInicio == horaFim and minutoInicio < minutoFim:
    if minutoFim >=60:
        minuto = (minutoFim%60)-minutoInicio
        roundMinuto = minutoFim/60
        roundMinuto = int(roundMinuto)
        hora = 0+roundMinuto
        print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
    else:    
        minuto = minutoFim-minutoInicio
        print('O JOGO DUROU %.0f HORA(S)'%hora,'E %.0f MINUTO(S)'%minuto)
else:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')'''          