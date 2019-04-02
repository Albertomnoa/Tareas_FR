import numpy as np
import networkx as nx
import networkx as nx
from networkx.algorithms.flow import maximum_flow
from networkx.algorithms.flow import shortest_augmenting_path
from networkx.algorithms.flow import preflow_push
import datetime as dt
import pandas as pd
import statistics as stats
import winsound as snd

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


numero_intancias = 10
mediciones = 5
archivo_CSV = "Datost4.csv"
control_iteraciones = 0

generadores_grafos = {
    "fast_gnp_random_graph": nx.fast_gnp_random_graph,
    "binomial_graph": nx.binomial_graph,
    "erdos_renyi_graph": nx.erdos_renyi_graph
}

algoritmos_flujo = {
    "shortest_augmenting_path": shortest_augmenting_path,
    "maximum_flow": maximum_flow,
    "preflow_push": preflow_push
}

t_csv = {
    "grafo": [],"generador_grafo": [],
    "algoritmo_fm": [],"vertices": [],
    "densidad": [],"aristas": [],
    "f": [],"s": [],"media": [],
    "mediana": [],"varianza": [],
    "desv": []
}
for generador_grafo in generadores_grafos:
    for inst_g_n in [round(pow(2, value + 1))
                     for value in
                     range(7, 11 )]:

        for grafo in range(1, numero_intancias + 1):
            f = np.random.randint(1, high=(inst_g_n - 1), dtype="int")
            s = np.random.randint(1, high=(inst_g_n - 1), dtype="int")

            while s == f:
                f = np.random.randint(1, high=(inst_g_n - 1), dtype="int")
                s = np.random.randint(1, high=(inst_g_n - 1), dtype="int")

            if f > s:
                swapping = f
                f = s
                s = swapping

            Grafo = generadores_grafos[generador_grafo](inst_g_n, 0.21, seed=None)
            aristas = Grafo.number_of_edges()
            pesos_normalmente_distribuidos = np.random.normal(15, 0.2, aristas)
            loop = 0
            for (u, v) in Grafo.edges():
                Grafo.edges[u, v]["capacity"] = pesos_normalmente_distribuidos[loop]
                loop += 1
            for instancia_grafo in range(1, 6):
                for algoritmo_flujo in algoritmos_flujo:
                    tiempos_ejecucion = []
                    for medicion in range(1, mediciones + 1):
                        t_inicio = dt.datetime.now()
                        obj = algoritmos_flujo[algoritmo_flujo](Grafo, f, s, capacity="capacity")
                        t_fin = dt.datetime.now()
                        tiempo_consumido_segundos = (t_fin - t_inicio).total_seconds()
                        tiempos_ejecucion.append(tiempo_consumido_segundos)
                    media = stats.mean(tiempos_ejecucion)
                    if media == 0:
                        snd.Beep(frequency, duration)
                        raise ValueError("La media no puede ser 0 para esta tarea......")
                    print("iteración %s tiempo consumido promedio %s" % (control_iteraciones + 1, round(media, 4)))
                    control_iteraciones +=1
                    t_csv["grafo"].append("vertices" + str(inst_g_n) + "aristas" + str(aristas))
                    t_csv["generador_grafo"].append(generador_grafo)
                    t_csv["vertices"].append(inst_g_n)
                    t_csv["densidad"].append(round(nx.density(Grafo),5))
                    t_csv["aristas"].append(aristas)
                    t_csv["f"].append(f)
                    t_csv["s"].append(s)
                    t_csv["algoritmo_fm"].append(algoritmo_flujo)
                    t_csv["media"].append(round(media, 5))
                    t_csv["mediana"].append(round(stats.median(tiempos_ejecucion), 5))
                    t_csv["varianza"].append(round(stats.pvariance(tiempos_ejecucion,
                                                                   mu=media), 5))
                    t_csv["desv"].append(round(stats.pstdev(tiempos_ejecucion,
                                                            mu=media), 5))
                    tiempos_ejecucion = []
ds = pd.DataFrame(t_csv)
ds.to_csv(archivo_CSV, encoding="utf-8", index=None)