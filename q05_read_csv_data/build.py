# Default imports
import numpy as np

# Enter code here
def read_ipl_data_csv(path, dtype='|S50'):
    dtype = '|S50'
    ipl_matches_array = np.genfromtxt(path, dtype = dtype, delimiter = ',', skip_header = 1)
    #print(ipl_matches_array)
    return ipl_matches_array
#read_ipl_data_csv(path = './data/ipl_matches_small.csv',dtype = 'float64')
