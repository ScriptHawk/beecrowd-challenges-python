#Leia a hora inicial e a hora final de um jogo.
#A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

horaInicio, horaFim = input().split(' ')
horaInicio = int(horaInicio)
horaFim = int(horaFim)

hora = 0

if horaInicio > horaFim:
    while horaInicio < 24:
        horaInicio = horaInicio+1
        hora = hora+1
    hora = hora+horaFim
    print('O JOGO DUROU %.0f HORA(S)'%hora)        
elif horaFim > horaInicio:
    hora = horaFim-horaInicio
    print('O JOGO DUROU %.0f HORA(S)'%hora)
else: print ('O JOGO DUROU 24 HORA(S)')     