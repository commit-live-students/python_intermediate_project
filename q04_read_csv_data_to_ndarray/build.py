# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
dtype = None

# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    data = np.genfromtxt(path, delimiter = ',',dtype=dtype,skip_header=1)
    return data

read_csv_data_to_ndarray(path,dtype)
#type(data)
#print(data)
    
    
    


