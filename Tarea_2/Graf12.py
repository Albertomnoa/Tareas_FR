import networkx as nx
import matplotlib.pyplot as plot


A=nx.MultiDiGraph()
A.add_edge('A','A',    weight=2)
A.add_edge('A','B',    weight=2)
A.add_edge('A','C',    weight=2)
A.add_edge('B','B',    weight=2)
A.add_edge('B','C',    weight=2)
A.add_edge('B','D',    weight=2)
A.add_edge('C','C',    weight=2)
A.add_edge('C','D',    weight=2)
A.add_edge('C','E',    weight=2)
A.add_edge('D','D',    weight=2)
A.add_edge('D','E',    weight=2)
A.add_edge('D','F',    weight=2)
A.add_edge('E','E',    weight=2)
A.add_edge('E','F',    weight=2)
A.add_edge('E','F',    weight=4)
A.add_edge('F','F',    weight=2)
A.add_edge('F','A',    weight=2)


black=[('A','A' ),('A','B'),('A','C'),
   ('B','B'),('B','C'),('B','D'),('C','C'),('C','D'),('C','E'),
   ('D','D'),('D','E'),('D','F'),('E','E'),('E','F'),('E','F'),('F','A')]

bl=[('E','F')]
lista=['A','B','C','D','E'],['F']
#posicion=nx.shell_layout(A, nlist=lista, scale=0.50, center=None, dim=2)

#posicion=nx.random_layout(A, center=None, dim=2)

#posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

posicion=nx.spectral_layout(A, weight='distans', scale=0.50, center=None, dim=2)

#posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.30, center=None, dim=2)

#posicion=nx.spring_layout(A, k=1, iterations=200, threshold=0.0001, weight='weight', scale=0.5)

#posicion=nx.rescale_layout( pos , escala = 1 )

#posicion=nx.bipartite_layout(A, {'Marianao','Vedado','Habana Vieja'}, align='vertical', scale=1, center=None, aspect_ratio=1.3333333333333333)

nx.draw_networkx_nodes(A,posicion,
                       node_size=600, node_color= '#48b457')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=10, alpha=0.5,
edge_color='b',arrowsize=20)

nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='Black',arrowsize=20)
nx.draw_networkx_labels(A,posicion, font_size=14,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf12_spectral_layout.eps")
plot.show(A)