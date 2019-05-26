import networkx as nx
import matplotlib.pyplot as plot


A=nx.DiGraph()
A.add_edge('Pc1','Pc1')
A.add_edge('Pc1','Pc2')
A.add_edge('Pc1','Pc3')
A.add_edge('Pc1','Pc4')
A.add_edge('Pc1','Pc5')
A.add_edge('Pc1','Pc6')
A.add_edge('Pc1','Pc7')
nodes_reflex = {'Pc1'}
nodes_no_reflex = {'Pc2','Pc3','Pc4','Pc5','Pc6','Pc6','Pc7'}
posicion=nx.spring_layout(A)
nx.draw_networkx_nodes(A,posicion,nodelist=nodes_reflex,
                       node_size=500, node_color= 'r')
nx.draw_networkx_nodes(A,posicion,nodelist=nodes_no_reflex,
                       node_size=500, node_color= 'y')
nx.draw_networkx_edges(A,posicion, width=2)
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial')


plot.axis('off')
plot.savefig("Graf6.eps")
plot.show(A)

