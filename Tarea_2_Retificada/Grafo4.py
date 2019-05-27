import networkx as nx
import matplotlib.pyplot as plot

A=nx.DiGraph()
A.add_edge('Con','C',weight=0.8)
A.add_edge('F','C'  ,weight=0.8)
A.add_edge('C','D'  ,weight=3)
A.add_edge('C','Rx' ,weight=3)
lista=['Con','F','D','Rx'],['C']
nodes=['Con','F','D','Rx']

posicion=nx.shell_layout(A, nlist=lista, scale=0.8, center=None, dim=2)

nx.draw_networkx_nodes(A,posicion, node_size=700, nodelist=['C'],node_color= '#bbf1f0',alpha=1)
nx.draw_networkx_nodes(A,posicion, nodelist= ['Con','F','D','Rx'],node_size=600, node_color= '#6ed3c5',alpha=1)
nx.draw_networkx_edges(A,posicion, width=4,edge_color='#35665f')

nx.draw_networkx_labels(A,posicion, font_size=13,font_family='arial',
                        font_color='#147645', font_weight='bold')

plot.axis('off')    
plot.savefig("Graf4_shell_layout.eps")
plot.show(A)

