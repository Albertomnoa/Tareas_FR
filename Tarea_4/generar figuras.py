import random as rnd
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt






G=nx.binomial_graph(30, 0.30, seed=None)




plt.figure(figsize=(4,4))
position = nx.spring_layout(G, scale=5,iterations=200)
nx.draw_networkx_nodes(G, position, node_size=50, node_color="#093ea8", node_shape="8")
nx.draw_networkx_edges(G, position, width=0.5, edge_color='black' )


plt.axis("off")
plt.savefig("binomial_graph.png",bbox_inches='tight')
plt.savefig(  "binomial_graph.eps",bbox_inches='tight')
plt.show(G)