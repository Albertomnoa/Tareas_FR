import networkx as nx
import matplotlib.pyplot as plot


A=nx.MultiGraph()
A.add_edge('Tel_1','Tel_2', weight=2)
A.add_edge('Tel_1','Tel_2', weight=3)
A.add_edge('Tel_1','Tel_2', weight=4)
A.add_edge('Tel_1','Tel_3', weight=2)
A.add_edge('Tel_1','Tel_4', weight=4)
A.add_edge('Tel_2','Tel_4', weight=2)
A.add_edge('Tel_2','Tel_4', weight=3)
A.add_edge('Tel_2','Tel_3', weight=2)
A.add_edge('Tel_3','Tel_5', weight=2)
A.add_edge('Tel_3','Tel_5', weight=3)
A.add_edge('Tel_3','Tel_5', weight=4)
A.add_edge('Tel_5','Tel_6', weight=2)
A.add_edge('Tel_5','Tel_6', weight=3)
A.add_edge('Tel_1','Tel_6', weight=2)
A.add_edge('Tel_1','Tel_6', weight=3)
black=[('Tel_1','Tel_2' ),('Tel_1','Tel_3'),('Tel_2','Tel_4'),
   ('Tel_2','Tel_3'),('Tel_3','Tel_5'),('Tel_3','Tel_5'),
   ('Tel_5','Tel_6'),('Tel_1','Tel_6')]

red=[('Tel_1','Tel_2'),('Tel_2','Tel_4'),
   ('Tel_1','Tel_2'),('Tel_1','Tel_6'),('Tel_5','Tel_6')]
bl=[('Tel_1','Tel_2'),('Tel_3','Tel_5')]

lista=['Tel_1','Tel_2','Tel_3','Tel_4','Tel_5'],['Tel_6']
#posicion=nx.shell_layout(A, nlist=lista, scale=0.50, center=None, dim=2)

#posicion=nx.random_layout(A, center=None, dim=2)

#posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

posicion=nx.spectral_layout(A, weight='weight', scale=0.50, center=None, dim=2)

#posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.30, center=None, dim=2)

#posicion=nx.spring_layout(A, k=1, iterations=200, threshold=0.0001, weight='weight', scale=0.5)

#posicion=nx.rescale_layout( pos , escala = 1 )

#posicion=nx.bipartite_layout(A, {'Marianao','Vedado','Habana Vieja'}, align='vertical', scale=1, center=None, aspect_ratio=1.3333333333333333)

nx.draw_networkx_nodes(A,posicion,
                       node_size=1000, node_color= 'y')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=10, alpha=0.5,
edge_color='b')
nx.draw_networkx_edges(A, posicion, edgelist=red, width=5, alpha=0.5,
edge_color='r')
nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='Black')

nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf8_spectral_layout.eps")
plot.show(A)
