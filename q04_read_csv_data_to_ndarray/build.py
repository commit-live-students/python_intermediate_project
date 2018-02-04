# Default Imports
import numpy as np
from numpy import genfromtxt

path = "./data/ipl_matches_small.csv"

def read_csv_data_to_ndarray(path,dtype = np.float64):

    fp = open(path,'r')
    csv_data = genfromtxt(path, dtype, delimiter=',', skip_header = 1)

    return csv_data
