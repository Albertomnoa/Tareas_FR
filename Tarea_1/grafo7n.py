import networkx as nx
import matplotlib.pyplot as plot


A=nx.MultiGraph()
A.add_edge('Lisa','Marianao', weight=2)
A.add_edge('Marianao','Playa', weight=2)
A.add_edge('Marianao','Playa', weight=4)
A.add_edge('Playa','Vedado', weight=2)
A.add_edge('Vedado','Habana_Vieja', weight=2)
A.add_edge('Vedado','Habana_Vieja', weight=4)
A.add_edge('Vedado','Habana_Vieja', weight=5)
A.add_edge('Habana_Vieja','Habana_del_Este', weight=2)
A.add_edge('Habana_Vieja','Habana_del_Este', weight=4)

black=[('Lisa','Marianao' ),('Playa','Vedado'),('Vedado','Habana_Vieja'),
   ('Habana_Vieja','Habana_del_Este'),('Marianao','Playa')]
red=[('Marianao','Playa'),('Vedado','Habana_Vieja'),
   ('Habana_Vieja','Habana_del_Este')]
bl=[('Vedado','Habana_Vieja')]
posicion=nx.spring_layout(A)

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
plot.savefig("Graf7.eps")
plot.show(A)

