def imprimirRonda(lista,ronda):
    for jugador,stats in lista[ronda].items():
        print (f"{jugador} =", end= " ")
        print (" ")
        for event,value in stats.items():
            print(f" {event} : {value} ", end= " ")
        kills = stats["kills"]
        assists = stats["assists"]
        deaths = stats["deaths"]
        puntaje = kills * 3 + assists * 1 - (1 if deaths else 0)
        lista[ronda][jugador]["puntos"] = puntaje
        print("puntos : ", puntaje)
        print(" ")
    jugadores_ordenados = sorted(lista[ronda].items(), key=lambda x: x[1]["puntos"], reverse=True)
    mvp = jugadores_ordenados[0][0]
    print("El MVP de la ronda es: ",mvp)
    
    