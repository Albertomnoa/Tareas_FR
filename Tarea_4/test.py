import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np


df = pd.read_csv("DatosG.csv", index_col=None,usecols=[4,7,8,9,10,11,12],dtype={ 'Mediana': np.float64,'Grado': 'category','CoefAg':np.float64, 'CentCer': np.float64,'CentCag':  np.float64,
                                                                        'Excentricidad': 'category','PageRag': np.float64} )