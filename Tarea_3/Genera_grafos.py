import random as rnd
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
def Crear_Grafos(nombre, size, int_distancia):

    G=nx.Graph()
    nodes = []
    for i in range(size):
        nodes.append(i)
    print(nodes)
    for i in nodes:
        idx = nodes.index(i) + 1
        print(idx)
        for j in nodes[idx:len(nodes)]:
            if rnd.randint(0,80)==1:
                G.add_edge(i,j, distancia=rnd.randint(1, int_distancia))
    print(G.edges)

    df = pd.DataFrame()
    df = nx.to_pandas_adjacency(G, dtype=int, weight='distancia')
    df.to_csv(nombre+".csv", index=None, header=None)
    plt.figure(figsize=(15,15))
    position = nx.spring_layout(G, scale=5,iterations=200)
    nx.draw_networkx_nodes(G, position, node_size=50, node_color="#de8919", node_shape="<")
    nx.draw_networkx_edges(G, position, width=0.5, edge_color='black' )


    plt.axis("off")
    plt.savefig(nombre + ".png",bbox_inches='tight')
    plt.savefig(nombre + ".eps",bbox_inches='tight')
    plt.show(G)

Crear_Grafos("1NoDirigido",800, 20)

# def Crear_DiGrafos(nombre, size, int_distancia):
#
#    G=nx.DiGraph()
#    nodes = []
#    for i in range(size):
#        nodes.append(i)
#    print(nodes)
#    for i in nodes:
#        idx = nodes.index(i) + 1
#        print(idx)
#        for j in nodes[idx:len(nodes)]:
#            if rnd.randint(0,50)==1:
#                G.add_edge(i,j, distancia=rnd.randint(1,int_distancia))
#    print(G.edges)
#
#    df = pd.DataFrame()
#    df = nx.to_pandas_adjacency(G, dtype=int, weight='distancia')
#    df.to_csv(nombre+".csv", index=None, header=None)
#    plt.figure(figsize=(6, 6))
#    position = position = nx.spring_layout(G, scale=0.4,iterations=200)
#    nx.draw_networkx_nodes(G,position, node_size=100, node_color= 'y')
#    nx.draw_networkx_edges(G,position, width=1,edge_color='black', )
#
#
#    plt.axis("off")
#    plt.savefig(nombre + ".png")
#    plt.show(G)
# Crear_DiGrafos("5Dirigido",540, 15)


            