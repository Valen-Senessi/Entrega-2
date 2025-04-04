def imprimirRonda(lista,ronda):
    for jugador,stats in lista[ronda].items():
        print (f"{jugador} =", end= " ")
        print (" ")
        for event,value in stats.items():
            print(f" {event} : {value} ", end= " ")
        print (" ")