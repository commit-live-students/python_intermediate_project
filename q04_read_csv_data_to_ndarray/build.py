# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
from numpy import genfromtxt
def read_csv_data_to_ndarray(path, dtype= '|S100'):
        array= np.genfromtxt('./data/ipl_matches_small.csv', delimiter=',', dtype= '|S100', skip_header=1)

        return array    
read_csv_data_to_ndarray


