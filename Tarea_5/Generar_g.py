import numpy as np
import networkx as nx
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.flow import maximum_flow
from networkx.algorithms.flow import shortest_augmenting_path
from networkx.algorithms.flow import preflow_push
import datetime as dt
import pandas as pd
import statistics as stats
import winsound as snd








def leer_capacity(G):
    capacity=[]
    for (u, v) in G.edges():
      capacity.append(G.edges[u, v]["capacity"])
    return capacity

Grafo = nx.erdos_renyi_graph(20, 0.19, seed=None)
aristas = Grafo.number_of_edges()
pesos_normalmente_distribuidos = np.random.normal(12, 1.5, aristas)
loop = 0
for (u, v) in Grafo.edges():
    Grafo.edges[u, v]["capacity"] = pesos_normalmente_distribuidos[loop]
    loop += 1
df = pd.DataFrame()
df = nx.to_pandas_adjacency(Grafo, dtype=int, weight='capacity')
df.to_csv("Grafo5" + ".csv", index=None, header=None)
widths=[]
widths = leer_capacity(Grafo)
print(widths)
widths[:] = [(x -9)/1.5 for x in widths]
plt.figure(figsize=(15, 15))
position = nx.kamada_kawai_layout(Grafo, scale=6 )
nx.draw_networkx_nodes(Grafo, position, node_size=500, node_color="#de8919", node_shape="8")
nx.draw_networkx_edges(Grafo, position, width=widths, edge_color='black')
# nx.draw_networkx_edge_labels(G, position, font_size=7, label_pos=.5)
nx.draw_networkx_labels(Grafo, position, font_size=10)

plt.axis("off")
plt.savefig("Grafo" + ".png", bbox_inches='tight')
plt.savefig("Grafo" + ".eps", bbox_inches='tight')
plt.show(Grafo)


