import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pingouin as pg
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import csv
df = pd.read_csv("Datost4.csv", index_col=None,usecols=[1,2,3,4,9],dtype={'generador_grafo': 'category',
                                                                        'algoritmo_fm': 'category','vertices': 'category','densidad':np.float64, 'mediana': np.float64} )
modelo = ols('mediana_log ~ generador_grafo+algoritmo_fm+vertices+densidad+generador_grafo*algoritmo_fm+algoritmo_fm*vertices+vertices*densidad+generador_grafo*vertices+generador_grafo*densidad+algoritmo_fm*densidad',data=df).fit()
print(modelo.summary())
modelo_csv = open("Anova_Mult.csv", 'w')
aov_table = sm.stats.anova_lm(modelo, typ=2)
df1=pd.DataFrame(aov_table)
df1.to_csv("modelo.csv")
for column in range(0, df["densidad"].count()):
    pass
    if  df.iat[column, 3] >=0.2061  and df.iat[column, 3] < 0.20854:
        df.iat[column, 3] = 1
    elif df.iat[column, 3] >=0.20854 and df.iat[column, 3] < 0.21098:
        df.iat[column, 3] = 2
    else:
        df.iat[column, 3] = 3
print(df["densidad"])
df['densidad'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["densidad"])
logX = np.log1p(df['mediana'])
df = df.assign(mediana_log=logX.values)
df.drop(['mediana'], axis= 1, inplace= True)

factores=["vertices","generador_grafo","densidad","algoritmo_fm"]
plt.figure(figsize=(8, 6))
for i in factores:
    print(rp.summary_cont(df['mediana_log'].groupby(df[i])))

    anova = pg.anova (dv='mediana_log', between=i, data=df, detailed=True , )
    pg._export_table (anova,("ANOVAs"+i+".csv"))

    ax=sns.boxplot(x=df["mediana_log"], y=df[i], data=df, palette="cubehelix")

    plt.savefig("boxplot_" + i + ".eps", bbox_inches='tight')
    tukey = pairwise_tukeyhsd(endog = df["mediana_log"], groups= df[i], alpha=0.05)

    tukey.plot_simultaneous(xlabel='Tiempo', ylabel=i)
    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
    plt.savefig("simultaneous_tukey" + i + ".eps", bbox_inches='tight')

    print(tukey.summary())
    t_csv = open("Tukey"+i+".csv", 'w')
    with t_csv:
        writer = csv.writer(t_csv)
        writer.writerows(tukey.summary())
        plt.show()


