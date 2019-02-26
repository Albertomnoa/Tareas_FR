import networkx as nx
import matplotlib.pyplot as plot


A=nx.MultiGraph()
A.add_edge('Lisa','Marianao', weight=2)
A.add_edge('Marianao','Playa', weight=2)
A.add_edge('Marianao','Playa', weight=4)
A.add_edge('Playa','Vedado', weight=2)
A.add_edge('Vedado','Habana Vieja', weight=2)
A.add_edge('Vedado','Habana Vieja', weight=4)
A.add_edge('Vedado','Habana Vieja', weight=5)
A.add_edge('Habana Vieja','Habana del Este', weight=2)
A.add_edge('Habana Vieja','Habana del Este', weight=4)

black=[('Lisa','Marianao' ),('Playa','Vedado'),('Vedado','Habana Vieja'),
   ('Habana Vieja','Habana del Este'),('Marianao','Playa')]
red=[('Marianao','Playa'),('Vedado','Habana Vieja'),
   ('Habana Vieja','Habana del Este')]
bl=[('Vedado','Habana Vieja')]

lista=['Lisa','Marianao','Playa','Vedado','Habana Vieja'],['Habana del Este']

#posicion=nx.shell_layout(A, nlist=lista, scale=0.50, center=None, dim=2)

#posicion=nx.random_layout(A, center=None, dim=2)

#posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

#posicion=nx.spectral_layout(A, weight='distans', scale=0.40, center=None, dim=2)

#posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.30, center=None, dim=2)

posicion=nx.spring_layout(A, k=1, iterations=200, threshold=0.0001, weight='weight', scale=0.5)

#posicion=nx.rescale_layout( pos , escala = 1 )

#posicion=nx.bipartite_layout(A, {'Marianao','Vedado','Habana Vieja'}, align='vertical', scale=1, center=None, aspect_ratio=1.3333333333333333)

nx.draw_networkx_nodes(A,posicion,
                       node_size=800, node_color= 'y')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=10, alpha=0.5,
edge_color='b')
nx.draw_networkx_edges(A, posicion, edgelist=red, width=5, alpha=0.5,
edge_color='r')
nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='Black')
for p in posicion:  
    posicion[p][1] -= 0.01
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf7_spring_layout.eps")
plot.show(A)

