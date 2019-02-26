import networkx as nx
import matplotlib.pyplot as plot


A=nx.MultiDiGraph()
A.add_edge('Persona1','Persona2', weight=2)
A.add_edge('Persona1','Persona2', weight=3)
A.add_edge('Persona1','Persona2', weight=4)
A.add_edge('Persona1','Persona3', weight=2)
A.add_edge('Persona1','Persona4', weight=4)
A.add_edge('Persona2','Persona4', weight=2)
A.add_edge('Persona2','Persona4', weight=3)
A.add_edge('Persona4','Persona3', weight=3)
A.add_edge('Persona3','Persona2', weight=2)
A.add_edge('Persona3','Persona5', weight=2)
A.add_edge('Persona3','Persona5', weight=3)
A.add_edge('Persona3','Persona5', weight=4)
A.add_edge('Persona5','Persona6', weight=2)
A.add_edge('Persona5','Persona6', weight=3)
A.add_edge('Persona1','Persona6', weight=2)
A.add_edge('Persona1','Persona6', weight=3)
black=[('Persona1','Persona2' ),('Persona1','Persona3'),('Persona2','Persona4'),
   ('Persona3','Persona2'),('Persona3','Persona5'),('Persona3','Persona5'),
   ('Persona5','Persona6'),('Persona1','Persona6'),('Persona4','Persona3')]

red=[('Persona1','Persona2'),('Persona2','Persona4'),
   ('Persona1','Persona2'),('Persona1','Persona6'),('Persona5','Persona6')]
bl=[('Persona1','Persona2'),('Persona3','Persona5')]

lista=['Persona1','Persona2','Persona3','Persona4','Persona5'],['Persona6']
#posicion=nx.shell_layout(A, nlist=lista, scale=0.50, center=None, dim=2)

#posicion=nx.random_layout(A, center=None, dim=2)

#posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

#posicion=nx.spectral_layout(A, weight='distans', scale=0.45, center=None, dim=2)

posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.30, center=None, dim=2)

#posicion=nx.spring_layout(A, k=1, iterations=200, threshold=0.0001, weight='weight', scale=0.5)

#posicion=nx.rescale_layout( pos , escala = 1 )

#posicion=nx.bipartite_layout(A, {'Marianao','Vedado','Habana Vieja'}, align='vertical', scale=1, center=None, aspect_ratio=1.3333333333333333)

nx.draw_networkx_nodes(A,posicion,
                       node_size=500
                       , node_color= 'y')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=10, alpha=0.5,
edge_color='b')
nx.draw_networkx_edges(A, posicion, edgelist=red, width=5, alpha=0.5,
edge_color='r')
nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='#297033')
for p in posicion:  
    posicion[p][1]+= 0.07
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf11_kamada_kawai_layout.eps")
plot.show(A)