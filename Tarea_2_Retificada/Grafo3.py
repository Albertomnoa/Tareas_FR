import networkx as nx
import matplotlib.pyplot as plot

A=nx.Graph()
A.add_edge('Luis(15)','Maria(15)')
A.add_edge('Luis(15)','Luis(15)')
A.add_edge('Maria(15)','Yanet(17)')
A.add_edge('Yanet(17)','Yanet(17)')
A.add_edge('Maria(15)','Ferndo(16)')
A.add_edge('Ferndo(16)','Desisy(18)')
A.add_edge('Desisy(18)','Pedro(17)')
A.add_edge('Pedro(17)','Pedro(17)')
A.add_edge('Pedro(17)','Julia(18)')
A.add_edge('Pedro(17)','Rosi(16)')
A.add_edge('Ferndo(16)','Claudia(16)')
nodes_reflex = {'Luis(15)','Ferndo(16)','Julia(18)'}
nodes_no_reflex = {'Maria(15)','Yanet(17)','Rosi(16)','Desisy(18)',
                   'Pedro(17)','Claudia(16)'}

lista =['Luis(15)','Julia(18)','Yanet(17)','Rosi(16)','Desisy(18)','Claudia(16)'], ['Maria(15)','Ferndo(16)','Pedro(17)']


posicion=nx.kamada_kawai_layout(A, dist=None, pos=None, weight='weight', scale=0.5, center=None, dim=2)

nx.draw_networkx_nodes(A,posicion,nodelist=nodes_reflex,
                       node_size=1500, node_color= '#ea6767')
nx.draw_networkx_nodes(A,posicion,nodelist=nodes_no_reflex,
                       node_size=1500, node_color= 'y')
nx.draw_networkx_edges(A,posicion, width=4,edge_color='#85d9ce')

nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')

plot.axis('off')
plot.savefig("Graf3_kamada_kawai_layout.eps")
plot.show(A)
