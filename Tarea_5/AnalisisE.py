import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np


df = pd.read_csv("DatosG.csv", index_col=None,usecols=[4,7,8,9,10,11,12],dtype={ 'Mediana': np.float64,'Grado': np.int ,'CoefAg':np.float64, 'CentCer': np.float64,'CentCag':  np.float64,
                                                                        'Excentricidad': np.int ,'PageRag': np.float64} )

plt.figure(figsize=(8, 6))
n,b,p=plt.hist(df["Excentricidad"], bins=3, color="#adcb18", alpha=1, edgecolor = 'black',  linewidth=1)
    # df['densidad'].replace({1: 'placebo', 2: 'low', 3: 'high'}, inplace=True)

print("n %s" % n, end="\n\n")
print("bins %s" % b, end="\n\n")
print("patches %s" % p, end="\n\n")

plt.xlabel('Excentricidad')
plt.ylabel('Frecuencia de ocurencia')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')


plt.savefig("HistogramExcentricidad.eps", bbox_inches='tight')
# plt.savefig("HistogramCentCer.png", bbox_inches='tight')
plt.show()



