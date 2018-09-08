# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtype= np.float64):
    
    arr_of_small_csv = np.genfromtxt(path,dtype, skip_header =  1, delimiter = ',')
    
    a = np.set_printoptions(threshold = np.nan)
    
    return arr_of_small_csv
    
read_csv_data_to_ndarray(path)


