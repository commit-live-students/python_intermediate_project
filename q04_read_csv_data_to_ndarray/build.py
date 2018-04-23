# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
import csv
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtype = np.float64):
    
    #with open(path,'r') as c:
    ipl_numpy_array = np.genfromtxt(path, dtype=dtype, delimiter=',', skip_header=1) 
        #print(type(ipl_numpy_array))
    
           
    return ipl_numpy_array 



 





