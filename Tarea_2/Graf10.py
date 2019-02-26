import networkx as nx
import matplotlib.pyplot as plot


A=nx.MultiDiGraph()
A.add_edge('PR','A',    weight=2)
A.add_edge('A','LH',    weight=2)
A.add_edge('A','LH',    weight=4)
A.add_edge('LH','May',  weight=2)
A.add_edge('May','Mat', weight=2)
A.add_edge('May','Mat', weight=4)
A.add_edge('LH','May',  weight=4)
A.add_edge('LH','May',  weight=5)
A.add_edge('May','Mat', weight=5)
A.add_edge('Mat','C',   weight=2)
A.add_edge('Mat','C',   weight=4)

black=[('PR','A' ),('LH','May'),('May','Mat'),
   ('Mat','C'),('A','LH')]
red=[('A','LH'),('May','Mat'),
   ('Mat','C'),('LH','May')]
bl=[('May','Mat'),('LH','May')]
lista=['PR','A','Mat','May','LH'],['C']
#posicion=nx.shell_layout(A, nlist=lista, scale=0.50, center=None, dim=2)

#posicion=nx.random_layout(A, center=None, dim=2)

#posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

posicion=nx.spectral_layout(A, weight='distans', scale=0.50, center=None, dim=2)

#posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.30, center=None, dim=2)

#posicion=nx.spring_layout(A, k=1, iterations=200, threshold=0.0001, weight='weight', scale=0.5)

#posicion=nx.rescale_layout( pos , escala = 1 )

#posicion=nx.bipartite_layout(A, {'A','May','C'}, align='vertical', scale=0.5, center=None, aspect_ratio=1.3333333333333333)

nx.draw_networkx_nodes(A,posicion,
                       node_size=500, node_color= 'y')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=10, alpha=0.5,
edge_color='b')
nx.draw_networkx_edges(A, posicion, edgelist=red, width=5, alpha=0.5,
edge_color='r')
nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='Black')
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf10_spectral_layout.eps")
plot.show(A)