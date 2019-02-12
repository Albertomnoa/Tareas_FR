import networkx as nx
import matplotlib.pyplot as plot

A=nx.Graph()
A.add_edges_from([('R1','Sw1'),('Sw1','Sw2'),
                  ('Sw1','Sw3'),('Sw2','Pc2'),('Sw2','Pc3'),
                  ('Sw3','Pc4'),('Sw3','Pc5')])

posicion=nx.spring_layout(A)
nx.draw_networkx_nodes(A,posicion, node_size=800)
nx.draw_networkx_edges(A,posicion, width=2)
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial')


plot.axis('off')
plot.savefig("Graf1.eps")
plot.show(A)
