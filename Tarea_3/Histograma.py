import networkx as nx
import matplotlib.pyplot as plt
import numpy as nup
import pandas as pd

dr = pd.read_csv( "salid.csv" )
print(dr["media"][10:15])
fig,axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))
axes[0,0].hist(dr["media"][:5],bins=5, color="#932525", alpha=1, edgecolor = 'black',  linewidth=1)
axes[0,0].set_title(dr["algoritmo"][1])

axes[0,0].set_ylabel('Frecuencia de ocurrencia')
axes[0,1].hist(dr["media"][5:10],bins=5, color="#ee9110", alpha=1, edgecolor = 'black',  linewidth=1)
axes[0,1].set_title(dr["algoritmo"][6])

axes[0,1].set_ylabel('Frecuencia de ocurrencia')
axes[0,2].hist(dr["media"][10:15],bins=5,color="#adcb18", alpha=1, edgecolor = 'black',  linewidth=1)
axes[0,2].set_title(dr["algoritmo"][11])

axes[0,2].set_ylabel('Frecuencia de ocurrencia')
axes[1,0].hist(dr["media"][15:20],bins=5,color="#129f10", alpha=1, edgecolor = 'black',  linewidth=1)
axes[1,0].set_title(dr["algoritmo"][16])

axes[1,0].set_ylabel('Frecuencia de ocurrencia')
axes[1,1].hist(dr["media"][20:25],bins=5,color="#093ea8", alpha=1, edgecolor = 'black',  linewidth=1)
axes[1,1].set_title(dr["algoritmo"][21])

axes[1,1].set_ylabel('Frecuencia de ocurrencia ')
axes[1,2].set_axis_off()


plt.savefig("Histograma.eps",bbox_inches='tight')
plt.savefig("Histograma.png",bbox_inches='tight')
plt.show()
plt.clf()

size = (25 * dr["cant_arista"][5:10] / dr["cant_vertice"][5:10])
color_names = ["#932525", "#129f10", "#093ea8", "#adcb18", "#ee9110"]
figure, axes = plt.subplots(figsize=(8, 8))
axes.scatter(dr["media"][:5], dr["cant_vertice"][:5],
            s=size, c=color_names, marker="D",
            label="Make max clique graph", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][5:10], dr["cant_vertice"][5:10],
            s=size, c=color_names, marker="s",
            label="Betweenness centrality", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][10:15], dr["cant_vertice"][10:15],
            s=size, c=color_names, marker="8",
            label="Greedy color algorithm", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][15:20], dr["cant_vertice"][15:20],
            s=size, c=color_names, marker=">",
            label="Maximal matching", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][20:25], dr["cant_vertice"][20:25],
            s=size, c=color_names, marker="*",
            label="Dfs_tree", alpha=0.8, edgecolors='black')

axes.set_ylabel("Vertices ", fontsize=12, fontfamily="arial", fontweight="bold")
axes.set_xlabel("Tiempo de Ejecucion", fontsize=12, fontfamily="arial", fontweight="bold")
plt.ylim((min(dr["cant_vertice"])-30, max(dr["cant_vertice"]) + 30))

axes.legend()
plt.savefig("DiagramVertices.eps",bbox_inches='tight')
plt.savefig("DiagramVertices.png",bbox_inches='tight')
plt.show()

size = (25 * dr["cant_arista"][5:10] / dr["cant_vertice"][5:10])
color_names = ["#932525", "#129f10", "#093ea8", "#adcb18", "#ee9110"]
figure, axes = plt.subplots(figsize=(8, 8))
axes.scatter(dr["media"][:5], dr["cant_arista"][:5],
            s=size, c=color_names, marker="D",
            label="Make max clique graph", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][5:10], dr["cant_arista"][5:10],
            s=size, c=color_names, marker="s",
            label="Betweenness centrality", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][10:15], dr["cant_arista"][10:15],
            s=size, c=color_names, marker="8",
            label="Greedy color algorithm", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][15:20], dr["cant_arista"][15:20],
            s=size, c=color_names, marker=">",
            label="Maximal matching", alpha=0.8, edgecolors='black')
axes.scatter(dr["media"][20:25], dr["cant_arista"][20:25],
            s=size, c=color_names, marker="*",
            label="Dfs_tree", alpha=0.8, edgecolors='black')

axes.set_ylabel("Aritas ", fontsize=12, fontfamily="arial", fontweight="bold")
axes.set_xlabel("Tiempo de Ejecución", fontsize=12, fontfamily="arial", fontweight="bold")
plt.ylim((min(dr["cant_arista"])-30, max(dr["cant_arista"]) + 30))

axes.legend()
plt.savefig("Diagram de disperción(cantidad de Arcos).eps",bbox_inches='tight')
plt.savefig("Diagram de disperción.png",bbox_inches='tight')
plt.show()
