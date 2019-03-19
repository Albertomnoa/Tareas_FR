import networkx as nx
import matplotlib.pyplot as plot
import numpy as nup
from time import time
A=nx.DiGraph()
A.add_edge('Con','C')
A.add_edge('F','C')
A.add_edge('C','D')
A.add_edge('C','R x')

tiempo=[]

for i in range(30):
    tiempo_inicial = time()    
    for j in range(1600):
      d= list(nx.topological_sort(A))
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    tiempo.append(tiempo_ejecucion)
media=nup.mean(tiempo)
desv=nup.std(tiempo) 
print (tiempo, d, media,desv)#En segundos
posicion=nx.spring_layout(A)
nx.draw_networkx_nodes(A,posicion, node_size=500, node_color= 'grey',alpha=0.9)

nx.draw_networkx_edges(A,posicion, width=2,edge_color='black')
nx.draw_networkx_labels(A,posicion, font_size=11,font_family='arial',
                        font_color='y', font_weight='bold')


plot.axis('off')
plot.savefig("Graf4.eps")
plot.show(A)

