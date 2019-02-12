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

posicion=nx.spring_layout(A)

nx.draw_networkx_nodes(A,posicion,
                       node_size=500
                       , node_color= 'y')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=10, alpha=0.5,
edge_color='b')
nx.draw_networkx_edges(A, posicion, edgelist=red, width=5, alpha=0.5,
edge_color='r')
nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='Black')
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf11.eps")
plot.show(A)