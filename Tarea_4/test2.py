import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np


df = pd.read_csv("Datost4.csv", index_col=None,usecols=[1,2,3,4,9],dtype={'generador_grafo': 'category',
                                                                        'algoritmo_fm': 'category','vertices': 'category','densidad': np.float64, 'mediana': np.float64} )

plt.figure(figsize=(8, 6))
n,b,p=plt.hist(round(df["densidad"],5), bins=3, color="#adcb18", alpha=1, edgecolor = 'black',  linewidth=1)
    # df['densidad'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace=True)

print("n %s" % n, end="\n\n")
print("bins %s" % b, end="\n\n")
print("patches %s" % p, end="\n\n")

plt.xlabel('Densidad de grafo')
plt.ylabel('Frecuencia de ocurencia')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')


plt.savefig("boxplot.eps")
plt.show()
b = ['0.0656', '0.0713', '0.077',  '0.0827']
i = 0
arregl_densi = open("Arreglodensid.csv", "w+")
for valor in b:
    i += 1
    arregl_densi.write(valor)
    if i < len(b):
        arregl_densi.write(",")
arregl_densi.write("\r\n")
arregl_densi.close()
plt.show()


