# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"

def read_ipl_data_csv(path,dtype = '|S50'):
    numpy_array = np.genfromtxt(path,delimiter=',',dtype =dtype , skip_header=1)
    numpy_arry = np.array(numpy_array)
    return numpy_arry
