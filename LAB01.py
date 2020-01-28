import numpy as np 
import pandas as pd 
import matplotlib.pyplot as mpl 

dataset_1 = pd.read_csv("watch_test2_sample.csv")
dataset_1.drop_duplicates(inplace = True)
dataset_1.interpolate(inplace = True)
dataset_1.fillna(0,inplace = True)
accX = np.array(dataset_1.loc[:,"accelerateX"])
print(accX.mean())

