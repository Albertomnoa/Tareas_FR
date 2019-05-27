import networkx as nx
import matplotlib.pyplot as plot

A=nx.MultiDiGraph()

A.add_edge('Luis(15)','Luis(15)'    ,weight=2)
A.add_edge('Maria(15)','Yanet(17)'  ,weight=2)
A.add_edge('Yanet(17)','Yanet(17)'  ,weight=2)

A.add_edge('Maria(15)','Fernando(16)' ,weight=2)
A.add_edge('Fernando(16)','Desisy(18)',weight=3)
A.add_edge('Fernando(16)','Desisy(18)',weight=2)
A.add_edge('Pedro(17)','Pedro(17)'  ,weight=2)
A.add_edge('Pedro(17)','Julia(18)'  ,weight=2)
A.add_edge('Pedro(17)','Rosi(16)'   ,weight=3)
A.add_edge('Pedro(17)','Rosi(16)'   ,weight=2)
A.add_edge('Fernando(16)','Claudia(16)',weight=2)

nodes_reflex = {'Luis(15)','Fernando(16)','Julia(18)'}
nodes_no_reflex = {'Maria(15)','Yanet(17)','Rosi(16)','Desisy(18)',
                   'Pedro(17)','Claudia(16)'}

black=[('Maria(15)','Yanet(17)'),
  ('Maria(15)','Fernando(16)'),('Fernando(16)','Desisy(18)'),
  ('Yanet(17)','Julia(18)'),('Desisy(18)','Pedro(17)'),
  ('Pedro(17)','Julia(18)'),  ('Pedro(17)','Rosi(16)'),
  ('Fernando(16)','Claudia(16)')]

bl=[('Fernando(16)','Desisy(18)'),('Pedro(17)','Rosi(16)')]

lista=['Luis(15)','Julia(18)','Yanet(17)','Rosi(16)','Desisy(18)','Claudia(16)'], ['Maria(15)','Fernando(16)','Pedro(17)']

posicion=nx.circular_layout(A, scale=0.5, center=None, dim=2)

nx.draw_networkx_nodes(A,posicion,nodelist=nodes_reflex,
                       node_size=1800, node_color= '#ea6d6d')
nx.draw_networkx_nodes(A,posicion,nodelist=nodes_no_reflex,
                       node_size=1500, node_color= '#cde95b')
nx.draw_networkx_edges(A, posicion, edgelist=bl, width=5, alpha=0.5,
edge_color='b')
nx.draw_networkx_edges(A, posicion, edgelist=black, width=2,
edge_color='Black')
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='#4f5148', font_weight='bold')

plot.axis('off')
plot.savefig("Graf9_circular_layout.eps")
plot.show(A)