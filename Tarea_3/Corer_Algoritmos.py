import random as rnd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as nup
import datetime as dt
import pandas as pd
import os


datos = {
        "algoritmo": [],
        "grafo": [],
        "cant_vertice": [],
        "cant_arista": [],
        "media": [],
        "desv":[],
        "mediana":[]
        }

def Leer_grafos(nomb):
   dr = pd.read_csv( nomb , header = None)
   A = nx.from_pandas_adjacency(dr, create_using = nx.Graph())
   print(A.edges)
   A.name=(i)
   return (A)

def Leer_grafos_Di(nomb):
   dr = pd.read_csv( nomb , header = None)
   A= nx.from_pandas_adjacency(dr, create_using = nx.DiGraph())
   A.name = (i)
   print(A.edges)
   return (A)
    
def Betweenness_centrality(grafo):
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()
        for j in range(15):
            nx.betweenness_centrality(grafo)
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo) 
        
    
    datos["algoritmo"].append("betweenness_centrality")
    datos["grafo"].append(grafo.name)
    datos["cant_vertice"].append(grafo.number_of_nodes())
    datos["cant_arista"].append(grafo.number_of_edges())
    datos["media"].append(media)
    datos["desv"].append(desv)
    datos["mediana"].append(mediana)
    return datos
 
def dfs_tree(grafo):
    tiempo=[]
    tiempo_inicial = dt.datetime.now()
    for i in range(30):
        tiempo_inicial = dt.datetime.now()
        for j in range(1000):
            nx.dfs_tree(grafo)
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo)
    datos["algoritmo"].append("dfs_tree")
    datos["grafo"].append(grafo.name)
    datos["cant_vertice"].append(grafo.number_of_nodes())
    datos["cant_arista"].append(grafo.number_of_edges())
    datos["media"].append(media)
    datos["desv"].append(desv)
    datos["mediana"].append(mediana)
    return datos

def Greedy_color(grafo):
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()
        for j in range(1000):
            nx.greedy_color(grafo)
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo)
    datos["algoritmo"].append("greedy_color")
    datos["grafo"].append(grafo.name)
    datos["cant_vertice"].append(grafo.number_of_nodes())
    datos["cant_arista"].append(grafo.number_of_edges())
    datos["media"].append(media)
    datos["desv"].append(desv)
    datos["mediana"].append(mediana)
    return datos
def Maximal_matching(grafo):
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()
        for j in range(1000):
            nx.maximal_matching(grafo)
        tiempo_final = dt.datetime.now()
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo)
    datos["algoritmo"].append("Maximal_matching")
    datos["grafo"].append(grafo.name)
    datos["cant_vertice"].append(grafo.number_of_nodes())
    datos["cant_arista"].append(grafo.number_of_edges())
    datos["media"].append(media)
    datos["desv"].append(desv)
    datos["mediana"].append(mediana)
    return datos

def make_max_clique_graph(grafo):
    tiempo=[]
    for i in range(30):
        tiempo_inicial = dt.datetime.now()
        for j in range(15):
            nx.make_max_clique_graph(grafo)
        tiempo_final = dt.datetime.now()   
        tiempo_ejecucion = (tiempo_final - tiempo_inicial).total_seconds()
        tiempo.append(tiempo_ejecucion)
    
    media=nup.mean(tiempo)
    desv=nup.std(tiempo)
    mediana=nup.median(tiempo)
    datos["algoritmo"].append("make_max_clique_graph")
    datos["grafo"].append(grafo.name)
    datos["cant_vertice"].append(grafo.number_of_nodes())
    datos["cant_arista"].append(grafo.number_of_edges())
    datos["media"].append(media)
    datos["desv"].append(desv)
    datos["mediana"].append(mediana)
    return datos


listgrafoNoDi=["1NoDirigido.csv","2NoDirigido.csv","3NoDirigido.csv","4NoDirigido.csv","5NoDirigido.csv"]

for i in listgrafoNoDi:
   l=Leer_grafos(i)
   make_max_clique_graph(l)
for i in listgrafoNoDi:
   l=Leer_grafos(i)
   Betweenness_centrality(l)
for i in listgrafoNoDi:
   l=Leer_grafos(i)
   Greedy_color(l)
for i in listgrafoNoDi:
   l=Leer_grafos(i)
   Maximal_matching(l)
for i in listgrafoNoDi:
    l=Leer_grafos(i)
    dfs_tree(l)

df = pd.DataFrame(datos)
df.to_csv("salid.csv", index=None)
    
