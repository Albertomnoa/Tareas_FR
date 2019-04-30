import pandas as pd
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np
import pingouin as pg
import seaborn as sns
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import csv
df = pd.read_csv("DatosG.csv", index_col=None, usecols=[4,6,7,8,9,10,11,12],dtype={ 'Mediana': np.float64,'FlujoMax': np.int, 'Grado': np.int, 'CoefAg':np.float64,
                                                                        'CentCer': np.float64,'CentCag': np.float64,
                                                                        'Excentricidad': np.int,'PageRag': np.float64 } )


for column in range(0, df["PageRag"].count()):
    pass
    if  df.iat[column, 7] >=0.0187 and df.iat[column, 7] < 0.0507:
        df.iat[column, 7] = 1
    elif df.iat[column, 7] >=0.0507 and df.iat[column, 7] < 0.0827:
        df.iat[column, 7] = 2
    else:
        df.iat[column, 7] = 3
print(df["PageRag"])
df['PageRag'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["PageRag"])

for column in range(0, df["CoefAg"].count()):
    pass
    if  df.iat[column, 3] >=0 and df.iat[column, 3] < 0.33333333:
        df.iat[column, 3] = 1
    elif df.iat[column, 3] >=0.33333333 and df.iat[column, 3] < 0.66666667:
        df.iat[column, 3] = 2
    else:
        df.iat[column, 3] = 3
print(df["CoefAg"])
df['CoefAg'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["CoefAg"])

for column in range(0, df["CentCer"].count()):
    pass
    if  df.iat[column, 4] >=0.2603 and df.iat[column, 4] < 0.39193333:
        df.iat[column, 4] = 1
    elif df.iat[column, 4] >=0.39193333 and df.iat[column, 4] < 0.52356667:
        df.iat[column, 4] = 2
    else:
        df.iat[column, 4] = 3
print(df["CentCer"])
df['CentCer'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["CentCer"])

for column in range(0, df["CentCag"].count()):
    pass
    if  df.iat[column, 5] >=0 and df.iat[column, 5] < 0.19126667:
        df.iat[column, 5] = 1
    elif df.iat[column, 5] >=0.19126667 and df.iat[column, 5] < 0.38253333:
        df.iat[column, 5] = 2
    else:
        df.iat[column, 5] = 3
print(df["CentCag"])
df['CentCag'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["CentCag"])

for column in range(0, df["Grado"].count()):
    pass
    if  df.iat[column, 2] >=1 and df.iat[column, 2] < 3.66666667:
        df.iat[column, 2] = 1
    elif df.iat[column, 2] >=3.66666667 and df.iat[column, 2] < 6.33333333:
        df.iat[column, 2] = 2
    else:
        df.iat[column, 2] = 3
print(df["Grado"])
df['Grado'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["Grado"])

for column in range(0, df["Excentricidad"].count()):
    pass
    if  df.iat[column, 6] >=2 and df.iat[column, 6] < 3.33333333:
        df.iat[column, 6] = 1
    elif df.iat[column, 6] >=3.33333333 and df.iat[column, 6] < 4.66666667:
        df.iat[column, 6] = 2
    else:
        df.iat[column, 6] = 3
print(df["Excentricidad"])
df['Excentricidad'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
print(df["Excentricidad"])



logX = np.log1p(df['Mediana'])
df = df.assign(mediana_log=logX.values)
df.drop(['Mediana'], axis= 1, inplace= True)

factores=["Grado","CoefAg","CentCer","CentCag","Excentricidad","PageRag"]
plt.figure(figsize=(8, 6))
for i in factores:
    print(rp.summary_cont(df['FlujoMax'].groupby(df[i])))

    anova = pg.anova (dv='FlujoMax', between=i, data=df, detailed=True , )
    pg._export_table (anova,("ANOVAsFlujoMax"+i+".csv"))

    ax=sns.boxplot(x=df["FlujoMax"], y=df[i], data=df, palette="cubehelix")

    plt.savefig("boxplot_FlujoMax" + i + ".eps", bbox_inches='tight')
    tukey = pairwise_tukeyhsd(endog = df["FlujoMax"], groups= df[i], alpha=0.05)

    tukey.plot_simultaneous(xlabel='Flujo Maximo', ylabel=i)

    plt.savefig("simultaneous_tukey" + i + ".eps", bbox_inches='tight')

    print(tukey.summary())
    t_csv = open("TukeyFlujoMax"+i+".csv", 'w')
    with t_csv:
        writer = csv.writer(t_csv)
        writer.writerows(tukey.summary())
    plt.show()

modelo = ols('FlujoMax ~ Grado + CoefAg + CentCer + CentCag + Excentricidad + PageRag +'
             ' Grado*CoefAg + Grado*CentCer+ Grado*CentCag + Grado*Excentricidad + Grado*PageRag'
             '+CoefAg*CentCer + CoefAg*CentCag + CoefAg*Excentricidad + CoefAg*PageRag + '
             'CentCer*CentCag + CentCer*Excentricidad + CentCer*PageRag + CentCag*Excentricidad'
             ' + CentCag*PageRag + Excentricidad*PageRag' ,data=df).fit()
print(modelo.summary())
modelo_csv = open("Anova_MultFlujoMax.csv", 'w')
aov_table = sm.stats.anova_lm(modelo, typ=2)
df1=pd.DataFrame(aov_table)
df1.to_csv("modeloFlujoMax.csv")
