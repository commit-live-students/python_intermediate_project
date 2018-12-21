# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
import csv 
import numpy as np

def read_csv_data_to_ndarray(path , dtype):
    
    with open(path, 'r') as f:
        matches = list(csv.reader(f, delimiter=','))

    ipl_matches = np.array(matches[1:] , dtype=dtype)
    return ipl_matches


