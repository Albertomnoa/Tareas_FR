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
lista=['Pc2','Pc3','Pc4','Pc5','Pc6','Pc6','Pc7'], ['Pc1']

#posicion=nx.shell_layout(A, nlist=lista, scale=0.50, center=None, dim=2)

posicion=nx.random_layout(A, center=None, dim=2)

#posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

#posicion=nx.spectral_layout(A, weight='distans', scale=0.50, center=None, dim=2)

#posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.5, center=None, dim=2)

#posicion=nx.spring_layout(A, k=1, iterations=200, threshold=0.0001, weight='weight', scale=1)

#posicion=nx.rescale_layout( pos , escala = 1 )

#posicion=nx.bipartite_layout(A, {'Pc1'}, align='vertical', scale=1, center=None, aspect_ratio=1.3333333333333333)
nx.draw_networkx_nodes(A,posicion,nodelist=nodes_reflex,
                       node_size=500, node_color= 'r')
nx.draw_networkx_nodes(A,posicion,nodelist=nodes_no_reflex,
                       node_size=500, node_color= 'y')
nx.draw_networkx_edges(A,posicion, width=2)
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial')


plot.axis('off')
plot.savefig("Graf6_random_layout.eps")
plot.show(A)

