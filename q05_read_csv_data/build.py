# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter code here
def read_ipl_data_csv(path, dtype=np.float64):
    ipl_matches_array=np.genfromtxt(path, dtype, skip_header=1, delimiter=',')
    #print(ipl_matches_array.shape, ipl_matches_array)
    return(ipl_matches_array)
    
read_ipl_data_csv(path, '|S50' )


