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
    
def imprimirRankingFinal(lista):
    ranking_final = {}
    for ronda in range(5):
        for jugador,stats in lista[ronda].items():
            if(jugador in ranking_final):
                ranking_final[jugador]["kills"] += stats["kills"]
                ranking_final[jugador]["assists"] += stats["assists"]
                ranking_final[jugador]["deaths"] += int(stats["deaths"])
                jugadores_ordenados = sorted(lista[ronda].items(), key=lambda x: x[1]["puntos"], reverse=True)
                kills = stats["kills"]
                assists = stats["assists"]
                deaths = stats["deaths"]
                puntaje = kills * 3 + assists * 1 - (1 if deaths else 0)
                ranking_final[jugador]["puntos"] += puntaje
            else:
                ranking_final[jugador] = {"kills": 0, "assists": 0, "deaths": 0, "puntos": 0, "MVPs": 0}
                kills = stats["kills"]
                assists = stats["assists"]
                deaths = (1 if stats["deaths"] == True else 0)
                puntaje = kills * 3 + assists * 1 - (1 if deaths else 0)
                ranking_final[jugador]["kills"] = kills
                ranking_final[jugador]["assists"] = assists
                ranking_final[jugador]["deaths"] = deaths
                jugadores_ordenados = sorted(lista[ronda].items(), key=lambda x: x[1]["puntos"], reverse=True)
                ranking_final[jugador]["MVPs"] = 0
                ranking_final[jugador]["puntos"] = puntaje
        jugadores_ordenados = sorted(lista[ronda].items(), key=lambda x: x[1]["kills"] * 3 + x[1]["assists"] * 1 - (1 if x[1]["deaths"] else 0), reverse=True)
        mvp = jugadores_ordenados[0][0]
        ranking_final[mvp]["MVPs"] += 1
        ranking_ordenado = sorted(ranking_final.items(), key=lambda x: x[1]["puntos"], reverse=True)
    print("RANKING FINAL ORDENADO POR PUNTOS CON LOS VALORES TOTALES DE LAS 5 PARTIDAS: ")
    for jugador, stats in ranking_ordenado:
        print(f"Jugador '{jugador}': STATS = "
        f"(Kills totales: {stats['kills']}, Assists totales: {stats['assists']}, "
        f"Deaths totales: {stats['deaths']}, MVPs totales: {stats['MVPs']})"
        f" {stats['puntos']} puntos totales")