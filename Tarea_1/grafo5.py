import networkx as nx
import matplotlib.pyplot as plot


A=nx.DiGraph()
A.add_edge('Ana','Felix')
A.add_edge('Ana','Alberto')
A.add_edge('Alberto','Yanet')
A.add_edge('Alberto','Fernando')
A.add_edge('Yanet','Roger')
A.add_edge('Teresa)','Roger')
A.add_edge('Felix','Marta')
A.add_edge('Marta','Fernando')
A.add_edge('Yanet','Ana')
A.add_edge('Marta','Ana')

posicion=nx.spring_layout(A)

nx.draw_networkx_nodes(A,posicion,
                       node_size=500, node_color= 'y')
nx.draw_networkx_edges(A,posicion, width=2,edge_color='b')
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='Black', font_weight='bold')


plot.axis('off')
plot.savefig("Graf5.eps")
plot.show(A)
