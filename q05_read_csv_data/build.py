# %load q05_read_csv_data/build.py
# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype = np.float64):
    
    ipl_matches_array = np.genfromtxt(path, dtype= '|S50' , skip_header = 1, delimiter = ',')
    
    np.set_printoptions(threshold= 1)
    
    return ipl_matches_array
    
path =  './data/ipl_matches_small.csv'
read_ipl_data_csv(path)




