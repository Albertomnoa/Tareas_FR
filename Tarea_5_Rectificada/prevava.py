import networkx as nx
import matplotlib.pyplot as plt
import numpy as nup
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
dr = pd.read_csv( "salid.csv" )
print(dr["media"][10:15])


# fig,axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 6))
plt.hist(np.log1p(dr["media"][:5]),bins=5, color="#932525", alpha=1, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')

plt.savefig("Histograma1.eps",bbox_inches='tight')
plt.savefig("Histograma1.png",bbox_inches='tight')
plt.show()

plt.hist(np.log1p(dr["media"][5:10]),bins=5, color="#ee9110", alpha=1, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
# axes[0,1].set_title(dr["algoritmo"][6])

plt.savefig("Histograma2.eps",bbox_inches='tight')
plt.savefig("Histograma2.png",bbox_inches='tight')
plt.show()
# axes[0,1].set_ylabel('Frecuencia de ocurrencia')
plt.hist(np.log1p(dr["media"][10:15]),bins=5,color="#adcb18", alpha=1, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')
# axes[0,2].set_title(dr["algoritmo"][11])

plt.savefig("Histograma3.eps",bbox_inches='tight')
plt.savefig("Histograma3.png",bbox_inches='tight')
plt.show()
# axes[0,2].set_ylabel('Frecuencia de ocurrencia')
plt.hist(np.log1p(dr["media"][15:20]),bins=5,color="#129f10", alpha=1, edgecolor = 'black',  linewidth=1)
# axes[1,0].set_title(dr["algoritmo"][16])
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')

plt.savefig("Histograma4.eps",bbox_inches='tight')
plt.savefig("Histograma4.png",bbox_inches='tight')
plt.show()
# axes[1,0].set_ylabel('Frecuencia de ocurrencia')
plt.hist(np.log1p(dr["media"][20:25]),bins=5,color="#093ea8", alpha=1, edgecolor = 'black',  linewidth=1)
plt.ylabel('Frecuencia de ocurrencia')
plt.xlabel('Tiempo de Ejecucion')

plt.savefig("Histograma5.eps",bbox_inches='tight')
plt.savefig("Histograma5.png",bbox_inches='tight')
plt.show()
# axes[1,1].set_title(dr["algoritmo"][21])
#
# axes[1,1].set_ylabel('Frecuencia de ocurrencia ')
# axes[1,2].set_axis_off()




plt.clf()

size = (25 * dr["cant_arista"][5:10] / dr["cant_vertice"][5:10])
color_names = ["#932525", "#129f10", "#093ea8", "#adcb18", "#ee9110"]
figure, axes = plt.subplots(figsize=(10, 10))
axes.errorbar(dr["media"][:5], dr["cant_vertice"][:5], xerr=(dr["desv"][:5]+1), fmt='D',color="#932525", alpha=1, label="Make max clique graph")
# axes.scatter(dr["media"][:5], dr["cant_vertice"][:5],
#             s=size, c=color_names, marker="D",
#             label="Make max clique graph", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][5:10], dr["cant_vertice"][5:10], xerr=(dr["desv"][5:10]+1), fmt='s',color="#129f10", alpha=1,label="Betweenness centrality")
# axes.scatter(dr["media"][5:10], dr["cant_vertice"][5:10],
#             s=size, c=color_names, marker="s",
#             label="Betweenness centrality", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][10:15], dr["cant_vertice"][10:15], xerr=(dr["desv"][10:15]+1), fmt='8',color="#093ea8", alpha=1,label="Greedy color algorithm")
# axes.scatter(dr["media"][10:15], dr["cant_vertice"][10:15],
#             s=size, c=color_names, marker="8",
#             label="Greedy color algorithm", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][15:20], dr["cant_vertice"][15:20], xerr=(dr["desv"][15:20]+1), fmt='>',color="#adcb18", alpha=1,label="Maximal matching")
# axes.scatter(dr["media"][15:20], dr["cant_vertice"][15:20],
#             s=size, c=color_names, marker=">",
#             label="Maximal matching", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][20:25], dr["cant_vertice"][20:25], xerr=(dr["desv"][20:25]+1), fmt='o',color="#ee9110", alpha=1,label="Dfs_tree")
# axes.scatter(dr["media"][20:25], dr["cant_vertice"][20:25],
#             s=size, c=color_names, marker="*",
#             label="Dfs_tree", alpha=0.8, edgecolors='black')

axes.set_ylabel("Vertices ", fontsize=12, fontfamily="arial", fontweight="bold")
axes.set_xlabel("Tiempo de Ejecucion", fontsize=12, fontfamily="arial", fontweight="bold")
plt.ylim((min(dr["cant_vertice"])-30, max(dr["cant_vertice"]) + 30))


# red_patch = mpatches.Patch(color='#932525', label='Grafo1')
# blu_patch = mpatches.Patch(color='#093ea8', label='Grafo3')
# gren_patch = mpatches.Patch(color='#129f10', label='Grafo2')
# naranja_patch = mpatches.Patch(color='#adcb18', label='Grafo5')
# amarrillo_patch = mpatches.Patch(color='#ee9110', label='Grafo4')
# legend_elements = [
#     Line2D([0], [0], marker='D', color='w', label="Make max clique graph",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='s', color='w', label="Betweenness centrality",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='8', color='w', label="Greedy color algorithm",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='>', color='w', label="Maximal matching",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='*', color='w',  label="Dfs_tree",
#            markerfacecolor='black', markersize=15),red_patch,gren_patch ,blu_patch, amarrillo_patch, naranja_patch]
# axes.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

axes.legend()
plt.savefig("DiagramVertices.eps",bbox_inches='tight')
plt.savefig("DiagramVertices.png",bbox_inches='tight')


size = (25 * dr["cant_arista"][5:10] / dr["cant_vertice"][5:10])
color_names = ["#932525", "#129f10", "#093ea8", "#adcb18", "#ee9110"]
figure, axes = plt.subplots(figsize=(10, 10))

axes.errorbar(dr["media"][:5], dr["cant_arista"][:5], xerr=(dr["desv"][:5]+1), fmt='D',color="#932525", alpha=1,label="Make max clique graph")
# axes.scatter(dr["media"][:5], dr["cant_arista"][:5],
#             s=size, c=color_names, marker="D",
#             label="Make max clique graph", alpha=0.8, edgecolors='black')

axes.errorbar(dr["media"][5:10], dr["cant_arista"][5:10], xerr=(dr["desv"][5:10]+1), fmt='s',color="#129f10", alpha=1,label="Betweenness centrality")
# axes.scatter(dr["media"][5:10], dr["cant_arista"][5:10],
#             s=size, c=color_names, marker="s",
#             label="Betweenness centrality", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][10:15], dr["cant_arista"][10:15], xerr=(dr["desv"][10:15]+1), fmt='8',color="#093ea8", alpha=1,label="Greedy color algorithm")
# axes.scatter(dr["media"][10:15], dr["cant_arista"][10:15],
#             s=size, c=color_names, marker="8",
#             label="Greedy color algorithm", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][15:20], dr["cant_arista"][15:20], xerr=(dr["desv"][15:20]+1), fmt='>',color="#adcb18", alpha=1,label="Maximal matching")
# axes.scatter(dr["media"][15:20], dr["cant_arista"][15:20],
#             s=size, c=color_names, marker=">",
#             label="Maximal matching", alpha=0.8, edgecolors='black')
axes.errorbar(dr["media"][20:25], dr["cant_arista"][20:25], xerr=(dr["desv"][20:25]+1), fmt='o',color="#ee9110", alpha=1,label="Dfs_tree")
# axes.scatter(dr["media"][20:25], dr["cant_arista"][20:25],
#             s=size, c=color_names, marker="*",
#             label="Dfs_tree", alpha=0.8, edgecolors='black')

axes.set_ylabel("Aritas ", fontsize=12, fontfamily="arial", fontweight="bold")
axes.set_xlabel("Tiempo de Ejecucion", fontsize=12, fontfamily="arial", fontweight="bold")
plt.ylim((min(dr["cant_arista"])-30, max(dr["cant_arista"]) + 30))


# red_patch = mpatches.Patch(color='#932525', label='Grafo1')
# blu_patch = mpatches.Patch(color='#093ea8', label='Grafo3')
# gren_patch = mpatches.Patch(color='#129f10', label='Grafo2')
# naranja_patch = mpatches.Patch(color='#adcb18', label='Grafo5')
# amarrillo_patch = mpatches.Patch(color='#ee9110', label='Grafo4')
# legend_elements = [
#     Line2D([0], [0], marker='D', color='w', label="Make max clique graph",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='s', color='w', label="Betweenness centrality",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='8', color='w', label="Greedy color algorithm",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='>', color='w', label="Maximal matching",
#            markerfacecolor='black', markersize=15),
#     Line2D([0], [0], marker='o', color='w',  label="Dfs_tree",
#            markerfacecolor='black', markersize=15),red_patch,gren_patch ,blu_patch, amarrillo_patch, naranja_patch]
# axes.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

axes.legend()
plt.savefig("DiagramAristas.eps",bbox_inches='tight')
plt.savefig("DiagramAristas.png",bbox_inches='tight')

axes.errorbar(dr["media"][:5], dr["cant_arista"][:5], xerr=dr["desv"][:5], fmt='+',color='k',alpha=1)
plt.show()
