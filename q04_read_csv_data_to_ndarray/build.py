# Default Imports
import numpy as np
#import pandas as pd
from numpy import genfromtxt
path1 = "./data/ipl_matches_small.csv"
dtype1 = '|S100'
def read_csv_data_to_ndarray(path2=path1,dtype2=dtype1):
    ipl_array = genfromtxt(path2, delimiter=',',dtype = dtype1,skip_header=1)
    #ipl_array = pd.read_csv('myfile.csv', sep=',',header=None)
    #ipl_array
    return ipl_array
#print read_csv_data_to_ndarray
