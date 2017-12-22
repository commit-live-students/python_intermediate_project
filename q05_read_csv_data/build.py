# Default imports
import numpy as np
import pandas as pd
from numpy import genfromtxt
path1 = "./data/ipl_matches_small.csv"
dtype1 = '|S50'
def read_ipl_data_csv(path2=path1,dtype=dtype1):
    ipl_matches_array = genfromtxt(path2, delimiter=',', dtype = '|S50', skip_header=1)
    return ipl_matches_array
