import numpy as np
import networkx as nx
import networkx as nx
import datetime as dt
import matplotlib.pyplot as plt
from networkx.algorithms.flow import shortest_augmenting_path

import datetime as dt
import pandas as pd
import statistics as stat
import winsound as snd


def Leer_grafos(nomb):
    dr = pd.read_csv((nomb+".csv"), header=None)
    A = nx.from_pandas_adjacency(dr)
    return A

def leer_capacity(G):
    capacity=[]
    for (u, v) in G.edges():
      capacity.append(G.edges[u, v]["weight"])
    return capacity


def Maxflow(G, a, b):
    tiempo_inicial = dt.datetime.now()
    # d =shortest_augmenting_path(G, a, b, capacity="weight")
    for i in range(40):
        d =shortest_augmenting_path(G, a, b, capacity="weight")
        print( dt.datetime.now())
    tiempo_final = (dt.datetime.now() - tiempo_inicial).total_seconds()
    return tiempo_final


def listnodos(d,f,s):
    for nodes in d.nodes():
        if d.nodes[nodes]!=f and d.nodes[nodes]!=s :
            nodos.append(nodes)
    return nodos
def Tiempos(G,nombre):
    df = {"Grafo": [], "Fuente": [], "Sumidero": [], "Media": [], "Mediana": [], "DesvStd": [], "flujoMax":
        [], "Grado": [], "CoefAg": [], "CentCer": [],"CentCag":[], "Excentricidad": [], "PageRag": []}
    Nodes = G.nodes
    print(Nodes)
    for i in Nodes:
        for j in Nodes:
            if i != j:
                t = []
                for k in range(10):
                    print(t, end="\n\n")
                    time = Maxflow(G, i, j)
                    t.append(time)
                PageRag = nx.pagerank(G, weight="capacity")
                df["Grafo"].append(nombre)
                df["Grado"].append(G.degree(i))
                df["CoefAg"].append(round(nx.clustering(G, i), 4))
                df["CentCer"].append(round(nx.closeness_centrality
                                           (G, i), 4))
                df["CentCag"].append(round(nx.load_centrality
                                           (G, i), 4))
                df["Excentricidad"].append(nx.eccentricity(G, i))
                df["PageRag"].append(round(PageRag[i], 4))
                df["Fuente"].append(i)
                df["Sumidero"].append(j)
                df["Media"].append(round(np.mean(t), 4))
                df["Mediana"].append(round(np.median(t), 4))
                df["DesvStd"].append(round(np.std(t), 4))
                df["flujoMax"].append(nx.maximum_flow_value
                                      (G, i, j, capacity="weight"))

    dd = pd.DataFrame(df)
    dd.to_csv(nombre+"D.csv", index=None)
G = Leer_grafos("Grafo1")
widths = []
widths = leer_capacity(G)
print(widths)
widths[:] = [(x - 7)/2 for x in widths]
plt.figure(figsize=(15, 15))
labels = {}
for u, v, data in G.edges(data=True):
    labels[(u, v)] = data['weight']
position = nx.kamada_kawai_layout(G, dist=None, pos=None, scale=0.5, center=None, dim=2)
nx.draw_networkx_nodes(G, position, node_size=800, node_color="#de8919", node_shape="8")
nx.draw_networkx_edges(G, position, width=widths, edge_color='black')
nx.draw_networkx_edge_labels(G, position, edge_labels=labels, font_size=10, label_pos=.5)
nx.draw_networkx_labels(G, position, font_size=15)

df = pd.DataFrame(position)
df.to_csv("position1" + ".csv", index=None, header=None)
plt.axis("off")
plt.savefig("Grafo1a" + ".png", bbox_inches='tight')
plt.savefig("Grafo1a" + ".eps", bbox_inches='tight')
plt.show(G)

d = shortest_augmenting_path(G, 4, 8, capacity="weight")
flowma = []
widths1 = []
widths0 = []
widths2 = []
widths3 = []
maxi = 0
nodos = []
nodosF = [4]
nodosS = [8]
nodos = listnodos(d, 4, 8)
for edges in d.edges():
    widths.append(d.edges[edges]["flow"])
    if d.edges[edges]["flow"] > 0:
        widths1.append(d.edges[edges]["capacity"])
        widths0.append(edges)
        flowma.append(d.edges[edges]['flow'])

    elif d.edges[edges]["flow"] == 0:
        widths2.append(edges)
        widths3.append(d.edges[edges]["capacity"])
print(widths1)
print(widths3)
flowma[:] = [x + 20 for x in flowma]
for i in flowma:
     if i > maxi:
        maxi = i
widths[:] = [x/10*x/6 for x in widths]
widths1[:] = [(x - 7)/2 for x in widths1]
widths3[:] = [(x - 7)/2 for x in widths3]
plt.figure(figsize=(15, 15))
position = pd.read_csv('position1.csv', header=None)
for u, v, data in d.edges(data=True):
    if data['flow'] >= 0:
     labels[(u, v)] = data['flow']
nx.draw_networkx_nodes(d, position,nodelist=nodos, node_size=800, node_color="#de8919", cnode_shape="8")
nx.draw_networkx_nodes(d, position, nodelist=nodosF,node_size=800, node_color="red", cnode_shape="8")
nx.draw_networkx_nodes(d, position,nodelist=nodosS, node_size=800, node_color="green", cnode_shape="8")

nx.draw_networkx_edges(d, position, edgelist=widths2, edge_color='black', width=widths3, arrows=False)
nx.draw_networkx_edges(d, position, edgelist=widths0, edge_cmap=plt.cm.Purples, width=widths1, edge_color=flowma,
                      edge_vmin=0, edge_vmax=maxi)

nx.draw_networkx_edge_labels(d, position, edge_labels=labels, font_size=10, label_pos=.5)
nx.draw_networkx_labels(d, position, font_size=15)

plt.axis("off")


plt.savefig("Grafo1cf" + ".png", bbox_inches='tight')
plt.savefig("Grafo1cf" + ".eps", bbox_inches='tight')

plt.show(G)
list=["Grafo1","Grafo2","Grafo3","Grafo4","Grafo5"]

for k in list:
    print(k)
    l = Leer_grafos(k)
    Tiempos(l,k)
  
