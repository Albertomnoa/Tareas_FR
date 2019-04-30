import numpy as np
import networkx as nx
import datetime as dt
import matplotlib.pyplot as plt
from networkx.algorithms.flow import shortest_augmenting_path
import scipy.stats as scipy
import datetime as dt
import pandas as pd
import statistics as stats
import winsound as snd


datos=["Grafo1D.csv", "Grafo2D.csv", "Grafo3D.csv", "Grafo4D.csv", "Grafo5D.csv"]
prop=["Grado", "CoefAg", "CentCer", "CentCag", "Excentricidad", "PageRag"]
for k in datos:
    df = pd.read_csv(k)
    dfil = df.groupby(["Fuente"]).median()
    cont=1
    for g in prop:


        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(1, 1, 1)
        count, bins, ignored = ax.hist(dfil[g],
                                       bins=len(dfil[g]), density=1,
                                       facecolor='#25e6ea', edgecolor="black", linewidth=0.2)
        ymax_val = max(count) + 1.5

        bincenters = 0.5*(bins[1:]+bins[:-1])

        mu = dfil[g].mean()
        sigma = round(stats.pstdev(dfil[g], mu), 2)

        y = scipy.norm.pdf(bincenters, mu, sigma)

        ax.plot(bincenters, y, 'r--', linewidth=2.5)

        ax.set_xlabel('Distribución de '+ g)
        ax.set_ylabel('Ocurrencia')

        ax.set_xlim(min(dfil[g]), max(dfil[g]))
        ax.set_ylim(0, ymax_val)
        ax.grid(True)
        cont+=1
        plt.savefig(g +k+".png", bbox_inches="tight", dpi=100)
        plt.savefig(g +k+".eps", bbox_inches="tight", dpi=100)
        plt.show()