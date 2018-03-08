# Import useful packages for the calculation of confidence intervvals
import pandas
import numpy as np
from scipy import stats
# Do not import tabulate from tabulate
import matplotlib.pyplot as plt
import matplotlib
#%matplotlib inline

# import data
filename = '../Data/train.csv'
titanic_dataframe = pandas.read_csv(filename)
titanic_dataframe.head()