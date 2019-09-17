# Default Imports
import numpy as np
from numpy import genfromtxt
path = "./data/ipl_matches_small.csv"

# Enter code here
def read_csv_data_to_ndarray(path,dtype ='np.float16'):
    d = np.genfromtxt(path,dtype,skip_header=1,delimiter = ',')
    return d
